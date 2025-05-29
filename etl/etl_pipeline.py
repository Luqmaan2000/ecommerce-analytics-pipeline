# %%
import os
import sqlite3
import pandas as pd
import requests

if os.path.exists("ecommerce.db"):
    os.remove("ecommerce.db")
    print("Old database deleted.")


conn = sqlite3.connect("ecommerce.db") #Creates (or connects to) a SQLite database file named `ecommerce.db`.
cursor = conn.cursor() #Creates a cursor object that allows you to run SQL commands through the connection.

with open("C:/Users/LUQMAAN/OneDrive/Documents/gitprojects/Ecommerce Analytics Pipeline/ecommerce-analytics-pipeline/sql/schema.sql","r") as f:
    schema_sql=f.read()#Opens the `schema.sql` file from the `sql/` folder and reads the entire SQL script into a Python string.

cursor.executescript(schema_sql) #Runs the full SQL script (with multiple statements) from the schema.sql file.
conn.commit() #Saves (commits) the changes to the database file.

print("Tables Created!")

# %%
df_users = pd.read_csv("C:/Users/LUQMAAN/OneDrive/Documents/gitprojects/Ecommerce Analytics Pipeline/ecommerce-analytics-pipeline/data/users.csv")
df_users.to_sql("users", conn, if_exists="append", index=False)

# Read products
df_products = pd.read_csv("C:/Users/LUQMAAN/OneDrive/Documents/gitprojects/Ecommerce Analytics Pipeline/ecommerce-analytics-pipeline/data/products.csv")
df_products.to_sql("products", conn, if_exists="append", index=False)

# Read orders
df_orders = pd.read_csv("C:/Users/LUQMAAN/OneDrive/Documents/gitprojects/Ecommerce Analytics Pipeline/ecommerce-analytics-pipeline/data/orders.csv")
df_orders.to_sql("orders", conn, if_exists="append", index=False)

print("CSV Data Loaded!")
# %%
url = "https://api.frankfurter.app/latest?from=GBP"
response = requests.get(url)
data = response.json()
rates = data["rates"]

# Step 2: Load users and orders from DB
users = pd.read_sql("SELECT user_id, currency FROM users", conn)
orders = pd.read_sql("SELECT * FROM orders", conn)

# Step 3: Merge users with orders
orders_merged = orders.merge(users, on="user_id", how="left")

# Step 4: Convert to GBP
def convert_to_gbp(row):
    rate = rates.get(row["currency"], 1)
    return row["total_amount_local"] / rate

orders_merged["total_amount_gbp"] = orders_merged.apply(convert_to_gbp, axis=1)
orders_merged["total_amount_gbp"] = orders_merged["total_amount_gbp"].round(2)

# Step 5: Save enriched table
orders_merged.to_sql("orders_enriched", conn, if_exists="replace", index=False)

print("Enrichment complete. orders_enriched table created.")


df = pd.read_sql("SELECT * FROM orders_enriched", conn)
print("\norders_enriched (preview):")
print(df.head())

df.to_csv("C:/Users/LUQMAAN/OneDrive/Documents/gitprojects/Ecommerce Analytics Pipeline/ecommerce-analytics-pipeline/data/orders_enriched.csv", index=False)