import os
import sys
import json
import pandas as pd
from sqlalchemy import text
from sqlalchemy import inspect
from sqlalchemy import create_engine
import numpy as np


engine = create_engine('postgresql+psycopg2://airflow:airflow@host.docker.internal:8585/postgres')

VEHICLE_SCHEMA = 'vehicle_schema.sql'
TRAJ_SCHEMA = 'trajectory_schema.sql'


class SqlUtils:

    @staticmethod
    def create_table():
        with engine.connect() as connection:
            for file in [VEHICLE_SCHEMA, TRAJ_SCHEMA]:
                with open(f'/postgres/{file}', 'r') as f:
                    query = text(f.read())
                    connection.execute(query)

    @staticmethod
    def insert_to_table(df: pd.DataFrame, table_name):
        with engine.connect() as connection:
            df.to_sql(name= table_name, con = connection, if_exists='replace', index=False)

    @staticmethod
    def get_tables():
        with engine.connect() as conncection:
            inspector = inspect(conncection)
            names = inspector.get_tables()
            return names
    
    @staticmethod
    def get_vehicles():
        with engine.connect() as conncection:
            vehicle_df = pd.read_sql_table('vehicles', con=conncection)
            return vehicle_df
    
    @staticmethod
    def get_traj():
        with engine.connect() as connection:
            traj_df = pd.read_sql_table('trajectories', con=connection)
            return traj_df
    
if __name__ == "__main__":
    print(get_tables())




