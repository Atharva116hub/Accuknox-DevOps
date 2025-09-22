import psutil
import logging
from datetime import datetime

logging.basicConfig(filename="system_health.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

CPU_THRESHOLD = 95.0
MEM_THRESHOLD = 95.0
DISK_THRESHOLD = 95.0

def check_system_health():
    alerts = []

    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"High CPU usage: {cpu_usage}%")

    memory = psutil.virtual_memory()
    if memory.percent > MEM_THRESHOLD:
        alerts.append(f"High Memory usage: {memory.percent}%")

    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        alerts.append(f"Low Disk Space: {disk.percent}% used")

    processes = len(psutil.pids())
    if processes > 300:
        alerts.append(f"Too many running processes: {processes}")

    print(f"\nSystem Stats:")
    print(f"  CPU Usage       : {cpu_usage}%")
    print(f"  Memory Usage    : {memory.percent}%")
    print(f"  Disk Usage      : {disk.percent}%")
    print(f"  Running Processes: {processes}")

    if alerts:
        for alert in alerts:
            print("[ALERT]", alert)
            logging.warning(alert)
    else:
        msg = "System running normally."
        print(msg)
        logging.info(msg)

if __name__ == "__main__":
    print(f"\n--- System Health Check @ {datetime.now()} ---")
    check_system_health()
