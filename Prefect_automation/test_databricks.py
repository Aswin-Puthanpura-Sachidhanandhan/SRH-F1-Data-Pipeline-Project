from dotenv import load_dotenv
import os
import requests

load_dotenv()

HOST = os.getenv("DATABRICKS_HOST")
TOKEN = os.getenv("DATABRICKS_TOKEN")
JOB_ID = os.getenv("JOB_ID")


url = f"{HOST}/api/2.1/jobs/run-now"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

payload = {
    "job_id": int(JOB_ID)
}

response = requests.post(
    url,
    headers=headers,
    json=payload
)

print("Status Code:", response.status_code)
print(response.text)