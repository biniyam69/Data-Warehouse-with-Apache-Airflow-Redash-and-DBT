# todo

from airflow import DAG
import os

from airflow.operators.bash_operator import BashOperator
from airflow_dbt.operators.dbt_operator import (
    DbtSeedOperator,
    DbtSnapshotOperator,
    DbtRunOperator,
    DbtTestOperator
)
from airflow.utils.dates import days_ago
cwd=os.getcwd()
DBT_FOLDER=f"{cwd}/../dbt/"
PROFILE_FOLDER=f"{cwd}/../dbt/"

default_args = {
  'dir': f'{DBT_FOLDER}',
  'start_date': days_ago(0),
  'retries':0,
  'dbt_bin':f'{DBT_FOLDER}',
  'profiles_dir':f'{PROFILE_FOLDER}/',
  'dir':f'{DBT_FOLDER}/'
}

with DAG(dag_id='dbt', default_args=default_args, schedule_interval='@daily') as dag:


    dbt_snapshot = DbtSnapshotOperator(
    task_id='dbt_snapshot',
    )

    dbt_run = DbtRunOperator(
    task_id='dbt_run',
    )

    dbt_test = DbtTestOperator(
    task_id='dbt_test',
    retries=0, 
    )

    dbt_snapshot >> dbt_run >> dbt_test