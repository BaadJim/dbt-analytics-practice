-- This test will fail if any sales amount is less than zero

SELECT 
    order_id,
    amount
FROM {{ ref('stg_sales') }}
WHERE amount < 0
