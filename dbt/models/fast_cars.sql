{{config (materialized='view')}}

with fast_cars as (
    SELECT * 
    from trajectories
    ORDER BY avg_speed DESC
    LIMIT 150

)

SELECT * FROM fast_cars