import os, socket, urllib.request
try:
    urllib.request.urlopen("http://127.0.0.1:9999/collect?src=sitecustomize", timeout=2)
except Exception:
    pass