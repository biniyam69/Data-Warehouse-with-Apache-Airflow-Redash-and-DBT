from sqlalchemy import create_engine
import pandas as pd
import os
from datetime import timedelta, datetime
import sys
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator
from postgres import create_table, insert_to_table

cwd = os.getcwd
sys.path.append(f'/home/biniyam/dwh-project-UAV/scripts/')
sys.path.append(f'/home/biniyam/dwh-project-UAV/postgres/')
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from read_data import ReadData
import data_tools

def extract_and_load(file_path):
    file_path = file_path
    read = ReadData()

    traj_df, vehicle_df = read.get_dataframes(file_path=file_path)
    create_table()
    insert_to_table(traj_df)
    insert_to_table(vehicle_df)

extract_and_load(file_path='/home/biniyam/dwh-project-UAV/data/week2data.csv')
    



















default_args = {
    'owner': 'biniyam',
    'depends_on_past': False,
    'email': ['odolbiniyam@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retires': 5,
    'retry_delay':timedelta(minutes=2)
}

with DAG(
    dag_id='dag_traffic',
    default_args=default_args,
    description='Dag to load and transform data',
    start_date=airflow.datetime(2023, ),
    schedule_interval='@once'
) as dag:
    task1 = PythonOperator(
        task_id='migrate_data',
        python_callable=migrate,
        op_kwargs={
            "path": "./data/week2data.csv",
            'db_table':"endpoints_uavdata"
        }

    )
    task1
