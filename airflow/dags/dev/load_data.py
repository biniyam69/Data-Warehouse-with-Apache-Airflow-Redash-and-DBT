from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2


def load_csv_to_pg():
    try:
        conn = psycopg2.connect(
            dbname='airflow',
            user='postgres',
            password='airflow',
            host='localhost',
            port='5432'
        )

        csv_path = '/home/biniyam/dwh-project-UAV/data/week2data.csv'

        # Load CSV into Pandas DataFrame
        df = pd.read_csv(csv_path)

        # Assuming table name is 'your_table_name' and you want to append data
        df.to_sql('airflow', conn, if_exists='append', index=False)

        conn.commit()
        conn.close()
        print("CSV data loaded into PostgreSQL successfully!")
    except Exception as e:
        print("Error:", e)


# Define Airflow DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 12, 1),
    'retries': 1,
}

dag = DAG('load_csv_to_pg_dag',
          default_args=default_args,
          schedule_interval='@daily')

# Define the PythonOperator
load_data_task = PythonOperator(
    task_id='load_data_task',
    python_callable=load_csv_to_pg,
    dag=dag,
)
