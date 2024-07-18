import pandas as pd
import sqlite3

def load_data():
    conn = sqlite3.connect("redbus.db")
    query = "SELECT * FROM redbuscsv"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
df = load_data()
df.to_csv("redbus_data.csv")