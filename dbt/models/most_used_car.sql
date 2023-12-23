{{config(materialized='view')}}

with used_car as (
    SELECT * FROM vehicles WHERE traveled_d>400
)

SELECT * 
FROM used_car