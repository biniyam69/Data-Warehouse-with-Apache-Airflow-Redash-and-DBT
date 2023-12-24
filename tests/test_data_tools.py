import pytest
import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# get the parent directory
project_root = os.path.abspath(os.path.join(current_dir, '..'))
# add the parent directory containing the module to the python path
sys.path.append(project_root)

from postgres.data_tools import SqlUtils

#create a fixture to initialize

@pytest.fixture
def sql_utils():
    return SqlUtils()

#and now the test cases

def test_create_table():
    #check if the tablees are created successfullt
    
    sql_utils = SqlUtils()
    sql_utils.create_table()
    tables = sql_utils.get_tables()
    assert 'vehicles' in tables
    assert 'trajectories' in tables

def test_insert(sql_utils):
    vehicle_data = {'track_id': [1, 2, 3], 'vehicle_type': ['Car', 'Truck', 'Motorcycle']}
    traj_data = {'track_id': [1, 2, 3], 'lat': [37.97, 37.98, 37.99], 'lon': [-122.05, -122.06, -122.07]}

    vehicle_df = pd.DataFrame(vehicle_data)
    traj_df = pd.DataFrame(traj_data)

    sql_utils.insert_to_table(vehicle_df, 'vehicles')
    sql_utils.insert_to_table(traj_df, 'trajectories')

    #check retrieved data
    vehicles=sql_utils.get_vehicles()
    trajectories = sql_utils.get_traj()

    assert vehicle_df.equals(vehicles)
    assert traj_df.equals(trajectories)