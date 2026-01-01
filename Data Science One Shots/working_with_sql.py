import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aryan@2005",
    database="registration_db",
    port=3307
)

data = pd.read_sql_query("SELECT * FROM users", conn)
print(data.sample(2))
print(f"\nShape of data: {data.shape[0]}")