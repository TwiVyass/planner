# 🗓️ AutoPlanner – Automated Weekly Task Scheduler

**AutoPlanner** is a lightweight Python-based automation tool that reads tasks from a CSV file, generates a well-formatted PDF summary, and uploads it to GitHub every Sunday at 9 PM using a cron job. It's designed to help individuals and teams maintain a consistent, version-controlled weekly task log without manual effort.

---

## 📁 Project Structure
planner/ 
├── planner.py # Core Python script to generate PDF
├── tasks.csv # Weekly task input file (CSV format) 
├── output/ # Folder for generated planner PDFs 
├── run_planner.sh # Shell script to automate the process 
├── venv/ # Python virtual environment 
├── planner_log.txt # Log file that records each PDF generation 
└── .git/ # Git repository


---

## ⚙️ Tools & Technologies Used

- **Languages:** Python, Bash
- **Libraries:** `fpdf`, `jinja2`, `pdfkit`
- **Version Control:** Git, GitHub
- **Task Scheduling:** Cron Jobs
- **Shell Scripting:** Automates weekly job execution
- **Environment:** Ubuntu via Windows Subsystem for Linux (WSL)

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

bash
git clone https://github.com/suhanasuffer/planner.git
cd planner
---

2️⃣ Set Up the Virtual Environment
sudo apt update
sudo apt install python3-venv wkhtmltopdf

python3 -m venv venv
source venv/bin/activate

pip install fpdf jinja2 pdfkit

3️⃣ Run the Planner Manually

python3 planner.py

Check the /output folder for a newly generated PDF.

4️⃣ Create and Use the Shell Script
Create a file called run_planner.sh and paste the following content:
#!/bin/bash
cd /home/your-username/planner
source venv/bin/activate
python3 planner.py >> cron_log.txt 2>&1
git add .
git commit -m "Weekly update"
git push

Make it executable:
chmod +x run_planner.sh


5️⃣ Set Up the Cron Job
Schedule the planner to run every Sunday at 9 PM:
crontab -e

Add this line (update the path to match your setup):
0 21 * * SUN /home/your-username/planner/run_planner.sh


6️⃣ Confirm and Monitor
Check if the cron job is scheduled:
crontab -l


Check logs if needed:
cat cron_log.txt


✅ Features
1. Automatically reads and formats weekly tasks from CSV
2. Generates a clean and professional PDF planner
3. GitHub integration for version control and team access
4. Automated weekly execution using cron
5. Logging feature records PDF generation events
6. Friendly CLI output for better UX
7. Handles missing or empty CSV gracefully

👥 Contributors
Suhani Thakur
Role: README, testing, bug fixes
GitHub: @suhanasuffer

Twsha Vyass
Role: Shell scripting, automation, cron setup
GitHub: @TwiVyass

🧠 License
This project is open-source and free to use for learning, improvement, and adaptation.

Feel free to contribute or fork the project for your own planning use!

---

### ✅ To Upload This to GitHub:
1. Save this content as `README.md` in your local `planner` directory.
2. Then run:
```bash
git add README.md
git commit -m "📘 Added full README with setup instructions"
git push






