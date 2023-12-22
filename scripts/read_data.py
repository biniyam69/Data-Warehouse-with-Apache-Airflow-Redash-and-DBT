import pandas as pd

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
            'unique_id': [],
            'track_id': [],
            'vehicle_type': [],
            'traveled_dis': [],
            'avg_speed': []
        }

        trajectories = {
            'unique_id': [],
            'lat': [],
            'lon': [],
            'speed': [],
            'lon_acc': [],
            'lat_acc': [],
            'time': []
        }



        for row_num, line in enumerate(lines):
            unique_id = self.get_unique_id(filename, row_num)
            line = line.split('; ')[:-1]
            assert len(line[4:]) % 6 == 0, f"{line}"
            vehicle["unique_id"].append(unique_id)
            vehicle["track_id"].append(int(line[0]))
            vehicle["vehicle_type"].append(line[1])
            vehicle["traveled_dis"].append(float(line[2]))
            vehicle["avg_speed"].append(float(line[3]))

            for i in range(0, len(line[4:]), 6):
                trajectories['unique_id'].append(unique_id)
                trajectories['lat'].append(float(lines[4+i+0]))
                trajectories['lon'].append(float(lines[4+i+1]))
                trajectories['speed'].append(float(lines[4+i+2]))
                trajectories['lon_acc'].append(float(lines[4+i+3]))
                trajectories['lat_acc'].append(float(lines[4+i+4]))

            

        vehicle_df = pd.DataFrame(vehicle).reset_index(drop=True)
        traj_df = pd.DataFrame(trajectories).reset_index(drop=True)
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


