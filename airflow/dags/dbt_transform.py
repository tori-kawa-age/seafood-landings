# airflow/dags/dbt_transform.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

DBT_DIR = "/opt/airflow/dbt/cold_chain_dw"

with DAG(
    dag_id="dbt_transform",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    BashOperator(
        task_id="dbt_run",
        bash_command=f"cd {DBT_DIR} && dbt deps && dbt seed && dbt run",
    )
    BashOperator(
        task_id="dbt_test",
        bash_command=f"cd {DBT_DIR} && dbt test",
    )
