#!/bin/bash
# Wrapper: runs the generic checker (shared image) or local python
if [ -f /checker/run.py ]; then
    python3 /checker/run.py
else
    echo "Checker runner not found. Use shared image."
    exit 1
fi
