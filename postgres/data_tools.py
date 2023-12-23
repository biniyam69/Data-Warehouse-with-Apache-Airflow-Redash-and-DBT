import pandas as pd
from sqlalchemy import create_engine, text, inspect

VEHICLE_SCHEMA = 'vehicle_schema.sql'
TRAJ_SCHEMA = 'trajectory_schema.sql'


class SqlUtils:
    def __init__(self) -> None:
        #  initialize the sqlalchemy engine
        self.engine = create_engine('postgresql+psycopg2://airflow:airflow@host.docker.internal:5432/postgres')

    def create_table(self):
        with self.engine.connect() as connection:
            for file in [VEHICLE_SCHEMA, TRAJ_SCHEMA]:
                with open(f'/postgres/{file}', 'r') as f:
                    query = text(f.read())
                    connection.execute(query)

    def insert_to_table(self, df: pd.DataFrame, table_name):
        with self.engine.connect() as connection:
            df.to_sql(name=table_name, con=connection, if_exists='replace', index=False)

    def get_tables(self):
        with self.engine.connect() as connection:
            inspector = inspect(connection)
            names = inspector.get_table_names()
            return names

    def get_vehicles(self):
        with self.engine.connect() as connection:
            vehicle_df = pd.read_sql_table('vehicles', con=connection)
            return vehicle_df

    def get_traj(self):
        with self.engine.connect() as connection:
            traj_df = pd.read_sql_table('trajectories', con=connection)
            return traj_df


if __name__ == "__main__":
    sql_utils = SqlUtils()
    
    try:
        #attempt to perform operations with the database
        sql_utils.create_table()
        tables = sql_utils.get_tables()
        print("Available tables:", tables)
        
        vehicles = sql_utils.get_vehicles()
        print("Vehicles data:", vehicles)
        
        trajectories = sql_utils.get_traj()
        print("Trajectories data:", trajectories)
    
    except Exception as e:
        print(f"Error: {e}")
