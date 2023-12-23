CREATE TABLE IF NOT EXISTS vehicles
(
    'id' SERIAL NOT NULL,
    'track_id' TEXT NOT NULL,
    'lat' TEXT NOT NULL,
    'lon' TEXT NOT NULL
    'speed' TEXT NOT NULL
    'lat_acc' TEXT NOT NULL
    'lon_acc' TEXT NOT NULL
    'time' TEXT NOT NULL
    
    PRIMARY KEY ('id')
    CONSTRAINT fk_trajectory
        FOREIGN KEY ("track_id")
        REFERENCES trajectories('track_id')
        ON DELETE CASCADE

);