# planner.py
import os
import subprocess
import csv
from datetime import datetime
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Weekly Planner", ln=1, align="C")
pdf.ln(10)

with open("tasks.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        line = f"{row['Date']}: {row['Task']}"
        pdf.cell(200, 10, txt=line, ln=1)

filename = f"output/weekly_planner_{datetime.now().date()}.pdf"
pdf.output(filename)
print(f"✅ Planner generated: {filename}")

os.chdir('/home/demo/planner')  # Changing directory to where your Git repo is
subprocess.run(['git', 'add', '.'])  # Adding all changes (PDF, CSV, etc.)
subprocess.run(['git', 'commit', '-m', 'Automated commit: New planner generated'])  # Committing changes
subprocess.run(['git', 'push', 'origin', 'main'])  # Pushing to the remote repository
