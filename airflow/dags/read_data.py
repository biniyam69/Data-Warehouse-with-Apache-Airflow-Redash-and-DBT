import pandas as pd

class ReadData:
    def __init__(self, path=None):
        self.file_path = path
    
    def read_file(self, path) -> list:

        with open(path, 'r') as f:
            lines = f.readlines()[1:]
            lines = list(map(lambda l: l.strip('\n'), lines))
            return lines
    
    def parse_data(self, lines, filename) -> tuple:
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
            unique_id = self.get_unique_id(filename, row_num)
            data = line.split('; ')
            assert len(data) >= 4, f"Incorrect data format: {data}"

            vehicle["track_id"].append(int(data[0]))
            vehicle["vehicle_type"].append(data[1])
            vehicle["traveled_dis"].append(float(data[2]))
            vehicle["avg_speed"].append(float(data[3]))

            for i in range(4, len(data), 6):
                trajectories['track_id'].append(unique_id)
                trajectories['lat'].append(float(data[i]))
                trajectories['lon'].append(float(data[i+1]))
                trajectories['speed'].append(float(data[i+2]))
                trajectories['lon_acc'].append(float(data[i+3]))
                trajectories['lat_acc'].append(float(data[i+4]))

        vehicle_df = pd.DataFrame(vehicle)
        traj_df = pd.DataFrame(trajectories)
        return vehicle_df, traj_df

    

    def get_dataframes(self, path):

        if not path and self.file_path:
            path = self.file_path

        lines = self.read_file(path)
        filename = path.split('/')[-1].strip('.csv')
        vehicle_df, traj_df = self.parse_data(lines, filename)


        return vehicle_df, traj_df
    
if __name__ == '__main__':
    ReadData(file_path='/home/biniyam/dwh-project-UAV/data/week2data.csv').get_dataframes()


