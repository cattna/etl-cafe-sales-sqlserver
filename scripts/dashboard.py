import streamlit as st
import pandas as pd
import pyodbc

st.title("📊 Dashboard Penjualan Cafe")

# Koneksi
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-91VLF6D2\\SQLEXPRESS;"
    "DATABASE=DB_CafeSales;"
    "Trusted_Connection=yes;"
)

df = pd.read_sql("SELECT * FROM SalesTransactions", conn)
st.dataframe(df)

st.bar_chart(df.groupby("item")["total_spent"].sum())
