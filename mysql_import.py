
import os
import pandas as pd
from sqlalchemy import create_engine

# Read database password from an environment variable
db_password = os.getenv("MYSQL_PASSWORD")

if not db_password:
    raise ValueError("Please set the MYSQL_PASSWORD environment variable.")

engine = create_engine(
    f"mysql+pymysql://root:{db_password}@localhost/online_food_delivery"
)

csv_file = "online_food_delivery_cleaned.csv"

if not os.path.exists(csv_file):
    raise FileNotFoundError(f"CSV file not found: {csv_file}")

df = pd.read_csv(csv_file)

print("CSV rows:", len(df))
print("CSV columns:", len(df.columns))

df.to_sql(
    name="food_orders",
    con=engine,
    if_exists="append",
    index=False
)

print("Data imported successfully!")
