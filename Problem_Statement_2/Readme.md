# Health Check Scripts

Python scripts to monitor application and system health with logging and console output.

---

## Files

- **app_health.py** – Checks the status of a web application (HTTP GET request) and logs to `app_health.log`.
- **system_health.py** – Monitors CPU, memory, disk usage, and running processes, logging warnings to `system_health.log`.

---

## Requirements

- Python 3.7+
- Install dependencies:
```bash
pip install requests psutil
Configuration
Application URL (optional):

bash
Copy code
export APP_URL="http://localhost:8000"
System thresholds (optional):

bash
Copy code
export CPU_THRESHOLD=90
export MEM_THRESHOLD=90
export DISK_THRESHOLD=90
export PROCESS_THRESHOLD=250
Usage
Run app health check:

bash
Copy code
python app_health.py
Run system health check:

bash
Copy code
python system_health.py
Logs:

Application: app_health.log

System: system_health.log

Example Output
pgsql
Copy code
--- Application Health Check ---
Application is UP (200)

--- System Health Check ---
CPU Usage: 25%
Memory Usage: 60%
Disk Usage: 70%
Processes: 120
System running normally.
