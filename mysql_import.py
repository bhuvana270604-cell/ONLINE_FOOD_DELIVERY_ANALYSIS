from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:bhuvana2004@localhost/online_food_delivery"
)

print("MySQL connection successful!")  



import os

csv_file = "online_food_delivery_cleaned.csv"

print("CSV file exists:", os.path.exists(csv_file))    




import pandas as pd
from sqlalchemy import create_engine

# MySQL connection
engine = create_engine(
    "mysql+pymysql://root:bhuvana2004@localhost/online_food_delivery"
)

# Read cleaned CSV
df = pd.read_csv("online_food_delivery_cleaned.csv")

print("CSV rows:", len(df))
print("CSV columns:", len(df.columns))

# Import data into MySQL
df.to_sql(
    name="food_orders",
    con=engine,
    if_exists="append",
    index=False
)

print("Data imported successfully!")   


import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:bhuvana2004@localhost/online_food_delivery"
)

df = pd.read_csv("online_food_delivery_cleaned.csv")

print("CSV rows:", len(df))

df.to_sql(
    name="food_orders_final",
    con=engine,
    if_exists="append",
    index=False
)