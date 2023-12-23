{{config(materialized='view')}}

with time_summary as (
    SELECT 
    time,
    Round(AVG(CAST(speed as numeric)), 2) as 'speed',
    Round(AVG(CAST(lat_acc as numeric)), 2) as 'lat_acc',
    Round(AVG(CAST(lon_acc as numeric)), 2) as 'lon_acc',
    from vehicles
    GROUP BY time ORDER BY time ASC

)

SELECT * FROM time_summary
