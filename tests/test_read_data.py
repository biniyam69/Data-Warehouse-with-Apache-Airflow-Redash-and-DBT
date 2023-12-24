import pytest
import pandas as pd
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# get the parent directory
project_root = os.path.abspath(os.path.join(current_dir, '..'))
# add the parent directory containing the module to the python path
sys.path.append(project_root)

from scripts.read_data import ReadData 

class TestReadData:

    @staticmethod
    def reader_instance():
        return ReadData(file_path='/home/biniyam/dwh-project-UAV/data/week2data.csv')
    

    def test_read_file(self):
        reader = ReadData()
        lines = reader.read_file('/home/biniyam/dwh-project-UAV/data/week2data.csv')
        assert isinstance(lines, list)
        assert len(lines) > 0
        assert len(lines) == 922

    def test_parse_data(self):
        reader = ReadData()
        lines = reader.read_file('/home/biniyam/dwh-project-UAV/data/week2data.csv')
        vehicle_df, traj_df = reader.parse_data(lines, 'week2data.csv')
        assert isinstance(vehicle_df, pd.DataFrame)
        assert isinstance(traj_df, pd.DataFrame)
        assert vehicle_df is not None
        assert traj_df is not None
        assert len(vehicle_df) > 0
        assert len(traj_df) > 0


    def test_get_df(self):
        reader = ReadData()
        vehicle_df, traj_df = reader.get_dataframes('/home/biniyam/dwh-project-UAV/data/week2data.csv')
        assert isinstance(vehicle_df, pd.DataFrame)
        assert isinstance(traj_df, pd.DataFrame)
        assert vehicle_df is not None
        assert traj_df is not None
        assert len(vehicle_df) > 0
        assert len(traj_df) > 0

    