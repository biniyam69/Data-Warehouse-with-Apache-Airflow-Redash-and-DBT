{[config(materialized='view')]}

with sum as (
    SELECT 
    type as 'Veh_type',
    COUNT (type) as 'Veh_count'
    ROUND(AVG(CAST(traveled_d as numeric)), 2) as 'average_dist'
    ROUND(AVG(CAST(avg_speed as numeric)), 2) as 'average_speed'
    from trajectories
    GROUP BY type ORDER BY 'Veh_count' ASC

)

SELECT * FROM sum