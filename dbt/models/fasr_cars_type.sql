{{config(materialized='view')}}

with fast_c as (SELECT * FROM {{ref('fast_cars')}})

SELECT 
type as 'vehicle_type'
COUNT(type) as 'vehicle_count'
from fast_c
GROUP BY type ORDER BY 'vehicle_count' ASC