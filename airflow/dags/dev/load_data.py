from sqlalchemy import create_engine
import pandas as pd
import os
from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'biniyam',
    'retires': 5,
    'retry_delay':timedelta(minutes=2)
}

def migrate(path, db_table):
    engine = create_engine('postgresql://airflow:airflow@localhost/airflow'
                           echo=True, future=True)
    
    print(os.system('pwd'))
    df = pd.read_csv(path, sep="[,;:]", index_col=False)
    df.to_sql(db_table, con=engine, if_exists='replace', index_label='id')

with DAG(
    dag_id='dag_traffic'
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
