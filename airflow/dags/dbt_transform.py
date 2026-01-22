# airflow/dags/dbt_transform.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

DBT_DIR = "/opt/airflow/dbt"

with DAG(
    dag_id="dbt_transform",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:
    # BashOperator(
    #     task_id="dbt_run",
    #     bash_command=f"cd {DBT_DIR} && dbt deps && dbt seed && dbt run",
    # )
    # BashOperator(
    #     task_id="dbt_test",
    #     bash_command=f"cd {DBT_DIR} && dbt test",
    # )
    # DBT_DIR = "/opt/airflow/dbt"

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"""
        set -euo pipefail
        cd {DBT_DIR}
        dbt deps
        dbt seed
        dbt run --profiles-dir {DBT_DIR} --target dev
        """,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"""
        set -euo pipefail
        cd {DBT_DIR}
        dbt test --profiles-dir {DBT_DIR} --target dev
        """,
    )

    dbt_run >> dbt_test

