{{ config(materialized='view') }}

SELECT 
    order_id,
    customer_id,
    order_date,
    amount
FROM {{ ref('raw_sales') }}
