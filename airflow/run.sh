#!/bin/bash

chmod -R 777 /opt/airflow/dags/
chmod -R 777 /opt/airflow/logs/
chmod -R 777 /opt/airflow/plugins/
chmod -R 777 /opt/airflow/config/
chmod -R 777 /opt/data/
chmod -R 777 /opt/dbt/
chmod -R 777 /opt/postgres/
chmod -R 777 /opt/scripts/

python3 /opt/airflow/dags/load_data.py
