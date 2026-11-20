# DevOps CTF - Local Practice System

## Overview
A local, single-user DevOps CTF practice lab mirroring terminal challenges from ctf.debuglife.id.
Each challenge is a self-contained folder with its own Dockerfile + docker-compose.yml.

Host: 192.168.1.202 (user docker12345, root same) - Ubuntu, Docker 29.6.

## Structure
```
/home/user/devops-ctf/
├── backend/main.py            # FastAPI + WebSocket PTY bridge + checker (host-side)
├── frontend/index.html        # 2-page UI (Challenge Browser + Workspace)
├── challenges/
│   ├── catalog.json           # 154 terminal challenges
│   ├── <slug>/                # per-challenge (self-contained)
│   │   ├── README.md          # title, desc, scenario, objective, hint, PoC, allowed/forbidden
│   │   ├── Dockerfile         # image khusus challenge
│   │   ├── docker-compose.yml # compose khusus challenge
│   │   ├── entrypoint.sh      # startup script
│   │   ├── config/            # file config rusak (target perbaikan)
│   │   └── checker/
│   │       └── rules.yaml     # allowed/forbidden + checks
│   └── ...
├── shared/checker/            # checker image (satu, generik)
├── start.sh / stop.sh
├── backend.log
└── README.md
```

## Operations
- Start:  ./start.sh  (backend on :8080)
- Stop:   ./stop.sh   (stops backend + all challenge containers)
- Logs:   tail -f backend.log
- UI:     http://192.168.1.202:8080

## How to add a new challenge
1. Create folder challenges/<slug>/ with Dockerfile, docker-compose.yml, config/, checker/rules.yaml, README.md.
2. Build: cd challenges/<slug> && echo docker12345 | sudo -S docker compose build
3. Restart backend (catalog already has slug/port): ./stop.sh && ./start.sh
4. Challenge now shows "Start" in UI.

## Built images (2)
- devops-ctf/python-keeps-phoning-home:latest (broken: beacon persistence)
- devops-ctf/nginx-upstream-port-and-app-token:latest (broken: wrong upstream port)

## Checker
- On-demand (only during Verify). Toggleable ON/OFF.
- Validates: forbidden files (sha256), http/command/process/grep/file_absent checks.
- Host-side execution via docker exec.

## Scoring
- Base: Beginner 10, Intermediate 25, Advanced 50.
- Checker ON: full. OFF: 0.5x.
- Paste penalty, WPM bonus, no-paste bonus.
- Surrender: partial (0.5 x progress).

## Features
- Start / Stop / Pause / Resume / Reset / Verify / Surrender
- Checker toggle ON/OFF
- WPM tracking (paste not counted)
- Paste count tracking
- Scoring + leaderboard
- 2-page UI (Challenge Browser + Workspace)
- Sidebar with scenario/objective/hint/allowed/forbidden/PoC
