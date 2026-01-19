# airflow/dags/ingest_fda_recalls.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def fetch_fda_recalls(**_):
    # call https://api.fda.gov/food/enforcement.json?search=...&limit=...
    # store raw json to S3 + upsert into raw.fda_enforcement_raw
    pass

with DAG(
    dag_id="ingest_fda_recalls",
    start_date=datetime(2025, 1, 1),
    schedule="0 8 * * 1",  # Mondays
    catchup=False,
) as dag:
    PythonOperator(task_id="fetch_fda", python_callable=fetch_fda_recalls)

