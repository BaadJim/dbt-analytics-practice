import duckdb
import polars as pl

# 1. Connect to the dbt-generated DuckDB file
# Setting read_only=True prevents file lock conflicts if dbt is running simultaneously
with duckdb.connect('dev.duckdb', read_only=True) as con:

    # 2. Execute SQL against your transformed dbt models and output to Polars
    df = con.sql("""
        SELECT * 
        FROM stg_sales 
        ORDER BY order_date DESC
    """).pl()

# 3. You are now back in native Polars territory
print(df.glimpse())

# Example Polars operation: Group by customer and sum amounts
summary = (
    df.group_by("customer_id")
    .agg(pl.col("amount").sum().alias("total_spent"),
         pl.col("order_id").count().alias("order_count"),
         (pl.col("amount").sum() / pl.col("order_id").count()).alias("avg_order_value"))
    .sort("total_spent", descending=True)
)

print(summary.head())