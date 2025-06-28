import streamlit as st
import pandas as pd
import pyodbc

st.title("📊 Dashboard Penjualan Cafe")

# Koneksi
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=your_server;"
    "DATABASE=your_database;"
)

df = pd.read_sql("SELECT * FROM SalesTransactions", conn)
st.dataframe(df)

st.bar_chart(df.groupby("item")["total_spent"].sum())
