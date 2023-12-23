CREATE TABLE IF NOT EXISTS vehicles
(
    track_id SERIAL PRIMARY KEY,
    type TEXT NOT NULL,
    traveled_d FLOAT DEFAULT NULL,
    avg_speed FLOAT DEFAULT NULL
);
