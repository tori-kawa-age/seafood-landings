FROM apache/airflow:2.10.3-python3.12

USER root
# If you need build deps for python packages (optional)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

USER airflow
# Install python dependencies (dbt + anything else)
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

