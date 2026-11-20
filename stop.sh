#!/bin/bash
cd /home/user/devops-ctf
if [ -f backend.pid ]; then
  kill $(cat backend.pid) 2>/dev/null && echo "backend stopped"
  rm -f backend.pid
fi
# stop all challenge containers
docker ps -q --filter name=devops-ctf- | xargs -r docker stop
docker ps -aq --filter name=devops-ctf- | xargs -r docker rm -f