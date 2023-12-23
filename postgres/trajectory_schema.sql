CREATE TABLE IF NOT EXISTS trajectories
(
    track_id SERIAL PRIMARY KEY,
    lat FLOAT NOT NULL,
    lon TEXT NOT NULL,
    speed REAL NOT NULL,
    lat_acc REAL NOT NULL,
    lon_acc REAL NOT NULL,
    time DATE NOT NULL
);
