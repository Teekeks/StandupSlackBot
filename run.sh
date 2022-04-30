#!/bin/bash

if [ ! -d "./venv" ]; then
  echo "Initial setup, creating venv..."
  python3 -m venv ./venv
  source ./venv/bin/activate
  pip install -r ./requirements.txt
else
  source ./venv/bin/activate
fi

python3 ./main.py

deactivate
