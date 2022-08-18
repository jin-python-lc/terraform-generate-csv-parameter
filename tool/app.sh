#!/bin/bash
cd ..
terraform show -json > tool/state.json
cd tool
python3 state.py