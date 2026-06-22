from prefect import flow, task
from dotenv import load_dotenv
import os
import requests

load_dotenv()

HOST = os.getenv("DATABRICKS_HOST")
TOKEN = os.getenv("DATABRICKS_TOKEN")
JOB_ID = os.getenv("JOB_ID")


@task
def trigger_databricks_job():

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

    response.raise_for_status()

    result = response.json()

    print(f"Triggered Run ID: {result['run_id']}")

    return result["run_id"]


@flow(name="F1 Automation Pipeline")
def f1_pipeline():

    run_id = trigger_databricks_job()

    print(f"Databricks Run Started: {run_id}")


if __name__ == "__main__":
    f1_pipeline()