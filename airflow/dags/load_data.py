from datetime import datetime, timedelta
import os
import sys
from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.append('/home/biniyam/dwh-project-UAV/scripts/')
sys.path.append('/home/biniyam/dwh-project-UAV/postgres/')


from read_data import ReadData
from data_tools import SqlUtils


def extract_and_load(file_path):
    read = ReadData()
    traj_df, vehicle_df = read.get_dataframes(file_path=file_path)
    return traj_df, vehicle_df


def create_table():
    SqlUtils.create_table()


def insert_vehicles_to_table(**kwargs):
    vehicle_df = kwargs['ti'].xcom_pull(task_ids='read_data', key='return_value')[1]
    SqlUtils.insert_to_table(vehicle_df, 'vehicles')


def insert_traj_to_table(**kwargs):
    traj_df = kwargs['ti'].xcom_pull(task_ids='read_data', key='return_value')[0]
    SqlUtils.insert_to_table(traj_df, 'trajectories')


default_args = {
    'owner': 'Biniyam',
    'depends_on_past': False,
    'email': ['odolbiniyam@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}

with DAG(
    dag_id='extract_load',
    default_args=default_args,
    description='DAG that loads and populates the data to SQL',
    start_date=datetime(2023, 12, 23), 
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    read_data = PythonOperator(
        task_id='read_data',
        python_callable=extract_and_load,
        op_kwargs={'file_path': '/home/biniyam/dwh-project-UAV/data/week2data.csv'},
        provide_context=True
    )

    create_table = PythonOperator(
        task_id='create_table',
        python_callable=create_table,
        provide_context=True
    )

    fill_vehicles = PythonOperator(
        task_id='fill_vehicles',
        python_callable=insert_vehicles_to_table,
        provide_context=True
    )

    fill_traj = PythonOperator(
        task_id='fill_traj',
        python_callable=insert_traj_to_table,
        provide_context=True
    )


    read_data >> create_table >> fill_vehicles >> fill_traj
