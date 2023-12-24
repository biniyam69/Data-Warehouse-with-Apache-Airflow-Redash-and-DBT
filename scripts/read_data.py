import pandas as pd
import numpy as np

class ReadData:
    def __init__(self, path=None):
        self.file_path = path


    def get_unique_id(self, filename, row_num):
        return f"{filename}_{row_num}"
    
    def read_file(self, path) -> list:

        with open(path, 'r') as f:
            lines = f.readlines()[1:]
            lines = list(map(lambda l: l.strip('\n'), lines))
            return lines
    
    def parse_data(self, lines,  filename) -> tuple:

        vehicle = {
            'track_id': [],
            'vehicle_type': [],
            'traveled_dis': [],
            'avg_speed': []
        }

        trajectories = {
            'track_id': [],
            'lat': [],
            'lon': [],
            'speed': [],
            'lon_acc': [],
            'lat_acc': [],
            'time': []
        }



        for row_num, line in enumerate(lines):
            line = line.split('; ')[:-1]
            assert len(line[4:]) % 6 == 0, f"{line}"
            vehicle["track_id"].append(int(line[0]))
            vehicle["vehicle_type"].append(line[1])
            vehicle["traveled_dis"].append(float(line[2]))
            vehicle["avg_speed"].append(float(line[3]))

        for i in range(4, len(line), 6):
            trajectories['track_id'].append(int(line[0]))
            
            lat = float(line[i])
            lon = float(line[i + 1])
            speed = float(line[i + 2])
            lon_acc = float(line[i + 3])
            lat_acc = float(line[i + 4])

           
            trajectories['lat'].append(lat)
            trajectories['lon'].append(lon)
            trajectories['speed'].append(speed)
            trajectories['lon_acc'].append(lon_acc)
            trajectories['lat_acc'].append(lat_acc)

        # making the lengths of the array equal by handling missing values
        max_length_vehicle = max(len(value) for value in vehicle.values())
        max_length_trajectories = max(len(value) for value in trajectories.values())

        #padding the lists to make them equal in length using numpy
        for key in vehicle:
            vehicle[key] += [np.nan] * (max_length_vehicle - len(vehicle[key]))
        for key in trajectories:
            trajectories[key] += [np.nan] * (max_length_trajectories - len(trajectories[key]))

        vehicle_df = pd.DataFrame(vehicle)
        traj_df = pd.DataFrame(trajectories)
        return vehicle_df, traj_df

            

        # vehicle_df = pd.DataFrame(vehicle).reset_index(drop=True)
        # traj_df = pd.DataFrame(trajectories).reset_index(drop=True)
        # return vehicle_df, traj_df
    

    def get_dataframes(self, path):

        if not path and self.file_path:
            path = self.file_path

        lines = self.read_file(path)
        filename = path.split('/')[-1].strip('.csv')
        vehicle_df, traj_df = self.parse_data(lines, filename)


        return vehicle_df, traj_df
    
if __name__ == '__main__':
    ReadData(file_path='/home/biniyam/dwh-project-UAV/data/week2data.csv').get_dataframes()


