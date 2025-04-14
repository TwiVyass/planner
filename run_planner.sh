#!/bin/bash

# Activate the virtual environment
source /home/demo/planner/venv/bin/activate

# Run the Python script to generate the PDF
python3 /home/demo/planner/planner.py

# Push updated files to GitHub
cd /home/demo/planner
git add .
git commit -m "Weekly update"
git push
