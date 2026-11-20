import asyncio
import json
import os
import pty
import subprocess
import termios
import threading
import time
from pathlib import Path

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# ---------- paths ----------
BASE = Path("/home/user/devops-ctf")
CATALOG = BASE / "challenges" / "catalog.json"
# fallback: catalog at BASE/challenges/catalog.json or BASE/catalog.json
if not CATALOG.exists():
    CATALOG = BASE / "catalog.json"
FRONTEND = BASE / "frontend"
STATE_FILE = BASE / "state.json"
ATTEMPTS_FILE = BASE / "attempts.json"
CHECKER_STATE_FILE = BASE / "checker_state.json"

app = FastAPI(title="DevOps CTF Local")

# serve local xterm.js (no CDN dependency)
_lib_dir = BASE / "frontend" / "lib"
if _lib_dir.exists():
    app.mount("/lib", StaticFiles(directory=str(_lib_dir)), name="lib")

# ---------- catalog ----------
_catalog = None
def load_catalog():
    global _catalog
    if _catalog is None:
        _catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    return _catalog

def reload_catalog():
    global _catalog
    _catalog = json.loads(CATALOG.read_text(encoding="utf-8"))

def find_challenge(cid):
    for c in load_catalog():
        if c["uuid"] == cid:
            return c
    return None

def challenge_dir(ch):
    slug = ch.get("slug")
    if not slug:
        return None
    return BASE / "challenges" / slug

def compose_file(ch):
    d = challenge_dir(ch)
    if d is None:
        return None
    p = d / "docker-compose.yml"
    return p if p.exists() else None

def container_name(cid):
    return "devops-ctf-" + cid[:8]

def exec_in_container(name, cmd, timeout=30):
    r = subprocess.run(["docker", "exec", name, "sh", "-c", cmd],
                       capture_output=True, text=True, timeout=timeout)
    return r

def run_checks_hostside(cid, ch):
    """Run checker on host via docker exec into the challenge container."""
    name = container_name(cid)
    cf = compose_file(ch)
    d = cf.parent if cf else None
    rules_path = (d / "checker" / "rules.yaml") if d else None
    result = {"passed": False, "results": [], "raw": ""}
    if rules_path is None or not rules_path.exists():
        result["results"].append({"id": "no_rules", "passed": False, "message": "rules.yaml not found"})
        result["passed"] = False
        return result

    try:
        import yaml
        rules = yaml.safe_load(rules_path.read_text(encoding="utf-8"))
    except Exception as e:
        result["results"].append({"id": "parse_error", "passed": False, "message": f"rules.yaml parse error: {e}"})
        result["passed"] = False
        return result

    results = []
    for f in rules.get("forbidden_files", []) or []:
        path = f.get("path")
        expected = f.get("sha256", "")
        if not path:
            continue
        r = exec_in_container(name, f"sha256sum {path} 2>/dev/null | awk '{{print $1}}'")
        actual = r.stdout.strip()
        if actual and actual != expected and expected:
            results.append({"id": "forbidden_modified", "passed": False,
                            "message": f"File yang dilarang diubah: {path}"})
        else:
            results.append({"id": "forbidden_ok", "passed": True, "message": "OK"})

    for c in rules.get("checks", []) or []:
        cid_check = c.get("id", "check")
        ctype = c.get("type")
        ok = False
        msg = c.get("message", "check failed")
        try:
            if ctype == "http":
                url = c.get("url", "")
                cmd = f"curl -s -o /dev/null -w '%{{http_code}}' {url} 2>/dev/null"
                r = exec_in_container(name, cmd)
                code = r.stdout.strip()
                ok = code == str(c.get("expect_status", 200))
            elif ctype == "command":
                cmd = c.get("cmd", "")
                r = exec_in_container(name, cmd)
                ok = r.stdout.strip() == str(c.get("expect_stdout", "")).strip()
            elif ctype == "process":
                pname = c.get("name", "")
                r = exec_in_container(name, f"pgrep -f '{pname}'")
                running = r.returncode == 0
                ok = running == c.get("should_run", True)
            elif ctype == "grep":
                fpath = c.get("file", "")
                pattern = c.get("pattern", "")
                r = exec_in_container(name, f"grep -c '{pattern}' {fpath} 2>/dev/null || echo 0")
                try:
                    count = int(r.stdout.strip().split(chr(10))[-1])
                except ValueError:
                    count = 0
                ok = count > 0
            elif ctype == "file_absent":
                path = c.get("path", "")
                r = exec_in_container(name, f"test -f {path} && echo EXISTS || echo ABSENT")
                ok = "ABSENT" in r.stdout
        except Exception as e:
            ok = False
            msg = f"{msg}: {e}"
        results.append({"id": cid_check, "passed": ok, "message": ("OK" if ok else msg)})

    passed = len(results) > 0 and all(r.get("passed") for r in results)
    if not results:
        passed = False
        results.append({"id": "no_checks", "passed": False, "message": "No checks defined in rules.yaml"})
    result["passed"] = passed
    result["results"] = results
    return result

# ---------- state helpers ----------
def load_json(path, default=None):
    if default is None:
        default = {}
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default

def save_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def get_state():
    return load_json(STATE_FILE, {})

def set_state(cid, status, port=None, paused_at=None):
    s = get_state()
    s[cid] = {"status": status, "port": port, "paused_at": paused_at, "updated": time.time()}
    save_json(STATE_FILE, s)

def get_checker_enabled(cid):
    cs = load_json(CHECKER_STATE_FILE, {})
    return cs.get(cid, True)

def set_checker_enabled(cid, enabled):
    cs = load_json(CHECKER_STATE_FILE, {})
    cs[cid] = bool(enabled)
    save_json(CHECKER_STATE_FILE, cs)

# ---------- docker helpers ----------
def run_cmd(cmd, cwd=None, timeout=300):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    return r

_RUNNING_CACHE = {"set": None, "ts": 0}
_PAUSED_CACHE = {"set": None, "ts": 0}

def get_running_set():
    global _RUNNING_CACHE
    if _RUNNING_CACHE["set"] is not None and time.time() - _RUNNING_CACHE["ts"] < 10:
        return _RUNNING_CACHE["set"]
    r = subprocess.run(["docker", "ps", "-q", "--filter", "name=devops-ctf-"],
                       capture_output=True, text=True)
    names = set()
    if r.returncode == 0:
        for cid_ in r.stdout.strip().splitlines():
            # get name
            r2 = subprocess.run(["docker", "inspect", "-f", "{{.Name}}", cid_],
                                capture_output=True, text=True)
            if r2.returncode == 0:
                names.add(r2.stdout.strip().lstrip("/"))
    _RUNNING_CACHE = {"set": names, "ts": time.time()}
    return names

def get_paused_set():
    global _PAUSED_CACHE
    if _PAUSED_CACHE["set"] is not None and time.time() - _PAUSED_CACHE["ts"] < 10:
        return _PAUSED_CACHE["set"]
    r = subprocess.run(["docker", "ps", "-q", "--filter", "name=devops-ctf-", "--filter", "status=paused"],
                       capture_output=True, text=True)
    names = set()
    if r.returncode == 0:
        for cid_ in r.stdout.strip().splitlines():
            r2 = subprocess.run(["docker", "inspect", "-f", "{{.Name}}", cid_],
                                capture_output=True, text=True)
            if r2.returncode == 0:
                names.add(r2.stdout.strip().lstrip("/"))
    _PAUSED_CACHE = {"set": names, "ts": time.time()}
    return names

def is_running(name):
    return name in get_running_set()

def is_paused(name):
    return name in get_paused_set()

def invalidate_container_cache():
    _RUNNING_CACHE["set"] = None
    _PAUSED_CACHE["set"] = None

_IMAGE_CACHE = {"set": None, "ts": 0}
def get_image_set():
    global _IMAGE_CACHE
    if _IMAGE_CACHE["set"] is not None and time.time() - _IMAGE_CACHE["ts"] < 60:
        return _IMAGE_CACHE["set"]
    r = subprocess.run(["docker", "images", "--format", "{{.Repository}}:{{.Tag}}"],
                       capture_output=True, text=True)
    s = set(r.stdout.strip().splitlines()) if r.returncode == 0 else set()
    _IMAGE_CACHE = {"set": s, "ts": time.time()}
    return s

def image_exists(img):
    return img in get_image_set()

def compose_up(ch, build=True):
    cf = compose_file(ch)
    if cf is None:
        raise HTTPException(400, "no compose file for this challenge")
    d = cf.parent
    cmd = ["docker", "compose", "-f", str(cf), "up", "-d"]
    if build:
        cmd.append("--build")
    r = run_cmd(cmd, cwd=d, timeout=600)
    if r.returncode != 0:
        raise HTTPException(500, "compose up failed: " + (r.stderr or r.stdout))
    return cf

def compose_down(ch, volumes=False):
    cf = compose_file(ch)
    if cf is None:
        return
    d = cf.parent
    cmd = ["docker", "compose", "-f", str(cf), "down"]
    if volumes:
        cmd.append("-v")
    run_cmd(cmd, cwd=d, timeout=120)

def compose_pause(ch):
    cf = compose_file(ch)
    if cf is None:
        return
    d = cf.parent
    run_cmd(["docker", "compose", "-f", str(cf), "pause"], cwd=d, timeout=60)

def compose_unpause(ch):
    cf = compose_file(ch)
    if cf is None:
        return
    d = cf.parent
    run_cmd(["docker", "compose", "-f", str(cf), "unpause"], cwd=d, timeout=60)

# ---------- attempts / scoring ----------
def load_attempts():
    return load_json(ATTEMPTS_FILE, {})

def save_attempt(cid, attempt):
    attempts = load_attempts()
    attempts.setdefault(cid, []).append(attempt)
    save_json(ATTEMPTS_FILE, attempts)

def calc_points(ch, checker_enabled, paste_count, avg_wpm, checks_passed, checks_total, surrendered=False):
    level = ch.get("level", "Beginner")
    base = {"Beginner": 10, "Intermediate": 25, "Advanced": 50}.get(level, 10)
    if surrendered:
        if checks_total > 0:
            return int(base * 0.5 * (checks_passed / checks_total))
        return 0
    mode_mult = 1.0 if checker_enabled else 0.5
    if checker_enabled:
        paste_mult = max(0.5, 1 - paste_count * 0.05)
    else:
        paste_mult = 1.0
    wpm_mult = 1.1 if (avg_wpm or 0) > 40 else 1.0
    nopaste_mult = 1.2 if paste_count == 0 else 1.0
    return int(base * mode_mult * paste_mult * wpm_mult * nopaste_mult)

# ---------- helpers ----------
def find_challenge(cid):
    for c in load_catalog():
        if c["uuid"] == cid:
            return c
    return None

def challenge_status(cid):
    name = container_name(cid)
    if is_paused(name):
        return "paused"
    if is_running(name):
        return "running"
    s = get_state().get(cid, {})
    return s.get("status", "not_started")

# ---------- API ----------
@app.get("/api/challenges")
def list_challenges(q: str = "", level: str = "", kind: str = "", topic: str = "", status: str = "", image: str = ""):
    done_set = set(load_json(BASE / "done.json", [])) if (BASE / "done.json").exists() else set()
    # done tracking via attempts (cleared)
    cleared = set()
    for cid, atts in load_attempts().items():
        if any(a.get("result") == "cleared" for a in atts):
            cleared.add(cid)

    out = []
    for c in load_catalog():
        if c.get("kind") != "Terminal":
            continue
        if q and q.lower() not in (c["title"] + " " + c.get("desc", "") + " " + " ".join(c.get("topics", []))).lower():
            continue
        if level and c.get("level", "").lower() != level.lower():
            continue
        if kind and c.get("kind", "").lower() != kind.lower():
            continue
        if topic and topic not in (c.get("topics") or []):
            continue
        if status:
            st = challenge_status(c["uuid"])
            if status == "todo" and st not in ("not_started",):
                continue
            if status == "done" and c["uuid"] not in cleared:
                continue
            if status == "paused" and st != "paused":
                continue
        cf = compose_file(c)
        has_image = cf is not None and (BASE / "challenges" / c.get("slug", "") / "Dockerfile").exists()
        # image existence check via docker
        slug = c.get("slug", "")
        img_name = f"devops-ctf/{slug}:latest"
        has_built = image_exists(img_name) if slug else False
        out.append({
            "uuid": c["uuid"],
            "title": c["title"],
            "level": c.get("level"),
            "kind": c.get("kind"),
            "topics": c.get("topics") or [],
            "desc": c.get("desc"),
            "time_limit": c.get("time_limit"),
            "has_image": has_built,
            "image": img_name,
            "running": is_running(container_name(c["uuid"])),
            "paused": is_paused(container_name(c["uuid"])),
            "status": challenge_status(c["uuid"]),
            "cleared": c["uuid"] in cleared,
            "slug": slug,
            "port": c.get("port"),
            "points": c.get("points", 10),
        })
    return {"count": len(out), "challenges": out}

@app.get("/api/challenges/{cid}")
def get_challenge(cid: str):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    slug = c.get("slug", "")
    img_name = f"devops-ctf/{slug}:latest"
    cf = compose_file(c)
    cleared = any(a.get("result") == "cleared" for a in load_attempts().get(cid, []))
    return {
        "uuid": c["uuid"],
        "title": c["title"],
        "level": c.get("level"),
        "kind": c.get("kind"),
        "topics": c.get("topics") or [],
        "desc": c.get("desc"),
        "scenario": c.get("scenario"),
        "objective": c.get("objective"),
        "hint": c.get("hint", ""),
        "poc": c.get("poc", ""),
        "allowed_files": c.get("allowed_files", []),
        "forbidden_files": c.get("forbidden_files", []),
        "time_limit": c.get("time_limit"),
        "has_image": image_exists(img_name) if slug else False,
        "image": img_name,
        "running": is_running(container_name(cid)),
        "paused": is_paused(container_name(cid)),
        "status": challenge_status(cid),
        "cleared": cleared,
        "slug": slug,
        "port": c.get("port"),
        "points": c.get("points", 10),
        "checker_enabled": get_checker_enabled(cid),
    }

@app.post("/api/challenges/{cid}/start")
def start_challenge(cid: str):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    cf = compose_file(c)
    if cf is None:
        raise HTTPException(400, "no compose file for this challenge")
    name = container_name(cid)
    if is_running(name):
        set_state(cid, "running", c.get("port"))
        return {"status": "already running", "container": name}
    if is_paused(name):
        compose_unpause(c)
        invalidate_container_cache()
        set_state(cid, "running", c.get("port"))
        return {"status": "resumed", "container": name}
    compose_down(c)  # clean stale
    compose_up(c, build=True)
    _IMAGE_CACHE["set"] = None
    invalidate_container_cache()
    set_state(cid, "running", c.get("port"))
    return {"status": "started", "container": name}

@app.post("/api/challenges/{cid}/stop")
def stop_challenge(cid: str):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    compose_down(c)
    invalidate_container_cache()
    set_state(cid, "not_started", c.get("port"))
    return {"status": "stopped", "container": container_name(cid)}

@app.post("/api/challenges/{cid}/pause")
def pause_challenge(cid: str):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    name = container_name(cid)
    if not is_running(name):
        raise HTTPException(400, "container not running")
    compose_pause(c)
    invalidate_container_cache()
    set_state(cid, "paused", c.get("port"), paused_at=time.time())
    return {"status": "paused", "container": name}

@app.post("/api/challenges/{cid}/resume")
def resume_challenge(cid: str):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    name = container_name(cid)
    if is_paused(name):
        compose_unpause(c)
    elif not is_running(name):
        compose_up(c, build=True)
    invalidate_container_cache()
    set_state(cid, "running", c.get("port"))
    return {"status": "resumed", "container": name}

@app.post("/api/challenges/{cid}/reset")
def reset_challenge(cid: str):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    compose_down(c, volumes=True)
    compose_up(c, build=True)
    invalidate_container_cache()
    _IMAGE_CACHE["set"] = None
    set_state(cid, "running", c.get("port"))
    return {"status": "reset", "container": container_name(cid)}

@app.post("/api/challenges/{cid}/verify")
async def verify_challenge(cid: str, request: Request):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    name = container_name(cid)
    if not is_running(name):
        raise HTTPException(400, "container not running")
    # parse body for paste_count, keystroke_count, elapsed_sec, avg_wpm, fastest_wpm
    try:
        body = await request.json()
    except Exception:
        body = {}
    paste_count = int(body.get("paste_count", 0))
    keystroke_count = int(body.get("keystroke_count", 0))
    elapsed_sec = float(body.get("elapsed_sec", 0))
    avg_wpm = float(body.get("avg_wpm", 0))
    fastest_wpm = float(body.get("fastest_wpm", 0))

    checker_enabled = get_checker_enabled(cid)
    if not checker_enabled:
        result = {"passed": True, "skipped": True, "message": "checker disabled", "results": []}
        checks_passed = 0
        checks_total = 0
        forbidden_violations = 0
    else:
        result = run_checks_hostside(cid, c)
        results = result.get("results", [])
        checks_total = len(results)
        checks_passed = sum(1 for x in results if x.get("passed"))
        forbidden_violations = sum(1 for x in results if x.get("id") == "forbidden_modified")

    passed = result.get("passed", False) if not result.get("skipped") else True
    points = calc_points(c, checker_enabled, paste_count, avg_wpm, checks_passed, checks_total, surrendered=False) if passed else 0

    attempt = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "result": "cleared" if passed else "failed",
        "checker_enabled": checker_enabled,
        "paste_count": paste_count,
        "keystroke_count": keystroke_count,
        "elapsed_sec": elapsed_sec,
        "avg_wpm": avg_wpm,
        "fastest_wpm": fastest_wpm,
        "points": points,
        "checks_passed": checks_passed,
        "checks_total": checks_total,
        "forbidden_violations": forbidden_violations,
    }
    save_attempt(cid, attempt)

    return {
        "passed": passed,
        "skipped": result.get("skipped", False),
        "message": result.get("message", ""),
        "results": result.get("results", []),
        "raw": result.get("raw", ""),
        "points": points,
        "paste_count": paste_count,
        "avg_wpm": avg_wpm,
        "fastest_wpm": fastest_wpm,
        "no_paste": paste_count == 0,
    }

@app.post("/api/challenges/{cid}/surrender")
async def surrender_challenge(cid: str, request: Request):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    name = container_name(cid)
    # run checker before stop (if enabled) to get progress
    checker_enabled = get_checker_enabled(cid)
    checks_passed = 0
    checks_total = 0
    if checker_enabled and is_running(name):
        cf = compose_file(c)
        if cf:
            d = cf.parent
            r = run_cmd(["docker", "compose", "-f", str(cf), "--profile", "checker", "run", "--rm", "checker"],
                        cwd=d, timeout=120)
            try:
                res = json.loads(r.stdout)
                results = res.get("results", [])
                checks_total = len(results)
                checks_passed = sum(1 for x in results if x.get("passed"))
            except Exception:
                pass
    # stop container
    compose_down(c)
    set_state(cid, "surrendered", c.get("port"))

    try:
        body = await request.json()
    except Exception:
        body = {}
    paste_count = int(body.get("paste_count", 0))
    keystroke_count = int(body.get("keystroke_count", 0))
    elapsed_sec = float(body.get("elapsed_sec", 0))
    avg_wpm = float(body.get("avg_wpm", 0))
    fastest_wpm = float(body.get("fastest_wpm", 0))

    points = calc_points(c, checker_enabled, paste_count, avg_wpm, checks_passed, checks_total, surrendered=True)

    attempt = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "result": "surrendered",
        "checker_enabled": checker_enabled,
        "paste_count": paste_count,
        "keystroke_count": keystroke_count,
        "elapsed_sec": elapsed_sec,
        "avg_wpm": avg_wpm,
        "fastest_wpm": fastest_wpm,
        "points": points,
        "checks_passed": checks_passed,
        "checks_total": checks_total,
        "forbidden_violations": 0,
    }
    save_attempt(cid, attempt)

    return {
        "result": "surrendered",
        "points": points,
        "checker_enabled": checker_enabled,
        "paste_count": paste_count,
        "avg_wpm": avg_wpm,
        "fastest_wpm": fastest_wpm,
        "checks_passed": checks_passed,
        "checks_total": checks_total,
        "poc": c.get("poc", ""),
    }

@app.post("/api/challenges/{cid}/checker")
async def toggle_checker(cid: str, request: Request):
    c = find_challenge(cid)
    if not c:
        raise HTTPException(404, "not found")
    try:
        body = await request.json()
    except Exception:
        body = {}
    enabled = bool(body.get("enabled", True))
    set_checker_enabled(cid, enabled)
    return {"uuid": cid, "checker_enabled": enabled}

@app.get("/api/challenges/{cid}/attempts")
def get_attempts(cid: str):
    return {"uuid": cid, "attempts": load_attempts().get(cid, [])}

@app.get("/api/progress")
def get_progress():
    attempts = load_attempts()
    total_points = 0
    cleared = set()
    surrendered = set()
    all_wpm = []
    fastest = 0
    for cid, atts in attempts.items():
        for a in atts:
            total_points += a.get("points", 0)
            if a.get("result") == "cleared":
                cleared.add(cid)
            if a.get("result") == "surrendered":
                surrendered.add(cid)
            if a.get("fastest_wpm"):
                fastest = max(fastest, a["fastest_wpm"])
            if a.get("avg_wpm"):
                all_wpm.append(a["avg_wpm"])
    return {
        "total_points": total_points,
        "cleared_count": len(cleared),
        "surrendered_count": len(surrendered),
        "total_challenges": len([c for c in load_catalog() if c.get("kind") == "Terminal"]),
        "avg_wpm": (sum(all_wpm) / len(all_wpm)) if all_wpm else 0,
        "fastest_wpm_global": fastest,
    }

@app.get("/api/containers")
def list_containers():
    r = subprocess.run(["docker", "ps", "--filter", "name=devops-ctf-", "--format", "{{.Names}}\t{{.Status}}"],
                       capture_output=True, text=True)
    rows = []
    for line in r.stdout.strip().splitlines():
        parts = line.split("\t")
        rows.append({"name": parts[0], "status": parts[1] if len(parts) > 1 else ""})
    return {"containers": rows}

# ---------- WebSocket terminal ----------
@app.websocket("/ws/terminal/{cid}")
async def terminal_ws(websocket: WebSocket, cid: str):
    await websocket.accept()
    c = find_challenge(cid)
    if not c:
        await websocket.send_text("Challenge not found.\r\n")
        await websocket.close()
        return
    name = container_name(cid)
    if not is_running(name):
        await websocket.send_text("Container not running. Start the challenge first.\r\n")
        await websocket.close()
        return

    import tty
    master, slave = pty.openpty()
    # Set host PTY to raw mode (disable echo, canonical, and all processing)
    # so only the container TTY handles echo + prompt + line editing
    tty.setraw(master)
    proc = subprocess.Popen(
        ["docker", "exec", "-it", "-e", "TERM=xterm", name, "/bin/sh"],
        stdin=slave, stdout=slave, stderr=slave,
        close_fds=True,
    )
    os.close(slave)
    # Re-apply raw mode after docker exec starts (docker may reset PTY settings)
    time.sleep(0.5)
    try:
        tty.setraw(master)
    except Exception:
        pass

    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    def reader():
        try:
            while True:
                try:
                    data = os.read(master, 4096)
                except OSError:
                    break
                if not data:
                    break
                # Filter out the "can't access tty" warning
                text = data.decode("utf-8", errors="replace")
                if "can't access tty" in text:
                    text = text.replace("/bin/sh: 0: can't access tty; job control turned off\r\n", "")
                    text = text.replace("/bin/sh: 0: can't access tty; job control turned off\n", "")
                    if not text:
                        continue
                    data = text.encode("utf-8", errors="replace")
                loop.call_soon_threadsafe(queue.put_nowait, data)
        except Exception as e:
            print(f"DEBUG reader error: {e}", flush=True)
        finally:
            loop.call_soon_threadsafe(queue.put_nowait, None)

    t = threading.Thread(target=reader, daemon=True)
    t.start()

    async def pump_out():
        while True:
            data = await queue.get()
            if data is None:
                break
            try:
                await websocket.send_bytes(data)
            except Exception:
                break

    async def pump_in():
        try:
            while True:
                msg = await websocket.receive()
                if msg.get("bytes") is not None:
                    os.write(master, msg["bytes"])
                elif msg.get("text") is not None:
                    text = msg["text"]
                    if text.startswith('{"type":"resize"'):
                        continue
                    os.write(master, text.encode())
        except WebSocketDisconnect:
            pass
        except Exception as e:
            print(f"DEBUG pump_in error: {e}", flush=True)

    try:
        await asyncio.gather(pump_out(), pump_in())
    finally:
        try:
            proc.terminate()
        except Exception:
            pass
        try:
            os.close(master)
        except Exception:
            pass

# ---------- static / pages ----------
@app.get("/")
def index():
    r = FileResponse(FRONTEND / "index.html")
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

@app.get("/challenge/{cid}")
def challenge_page(cid: str):
    r = FileResponse(FRONTEND / "index.html")
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)