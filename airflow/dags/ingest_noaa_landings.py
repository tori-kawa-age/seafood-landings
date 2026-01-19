# airflow/dags/ingest_noaa_landings.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os, json

def fetch_noaa_to_s3_and_pg(**_):
    # 1) call NOAA landings query tool / dataset extract
    # 2) write to S3: s3://<bucket>/raw/noaa/dt=YYYY-MM-DD/landings.json
    # 3) upsert into Postgres raw.noaa_landings_raw (jsonb payload + ingestion metadata)
    pass

with DAG(
    dag_id="ingest_noaa_landings",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    PythonOperator(
        task_id="fetch_noaa",
        python_callable=fetch_noaa_to_s3_and_pg,
    )

