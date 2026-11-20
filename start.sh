#!/bin/bash
cd /home/user/devops-ctf
# start backend
if [ -f backend.pid ] && kill -0 $(cat backend.pid) 2>/dev/null; then
  echo "backend already running (pid $(cat backend.pid))"
else
  nohup python3 -m uvicorn backend.main:app --host 0.0.0.0 --port 8080 > backend.log 2>&1 &
  echo $! > backend.pid
  echo "backend started (pid $!)"
fi
echo "UI: http://$(hostname -I | awk '{print $1}'):8080"