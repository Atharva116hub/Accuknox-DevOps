import requests
import logging
from datetime import datetime


logging.basicConfig(filename="app_health.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")


APP_URL = "http://localhost:8000"

def check_app_health():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == 200:
            msg = f"Application is UP ({response.status_code})"
            print(msg)
            logging.info(msg)
        else:
            msg = f"Application is DOWN (HTTP {response.status_code})"
            print(msg)
            logging.error(msg)
    except requests.exceptions.RequestException as e:
        msg = f"Application is DOWN (Error: {e})"
        print(msg)
        logging.error(msg)

if __name__ == "__main__":
    print(f"\n--- Application Health Check @ {datetime.now()} ---")
    check_app_health()
