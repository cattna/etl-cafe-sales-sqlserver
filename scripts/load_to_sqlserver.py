import pandas as pd
import pyodbc

# ✅ Perbaikan 1: Tanda kutip di path file
df = pd.read_excel(r"D:\github-etlproject\etl-coffee-pipeline-colab\data\clean_data_sales.xlsx")

# ✅ Perbaikan 2: Tambahkan Trusted_Connection agar bisa login Windows (jika pakai Windows Authentication)
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=LAPTOP-91VLF6D2\\SQLEXPRESS;"
    "DATABASE=DB_CafeSales;"
    "Trusted_Connection=yes;"
)

# Buat koneksi
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# ✅ Perbaikan 3: Pastikan kolom nama di Excel sesuai dengan script
# Kamu bisa print df.columns untuk memastikannya
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO SalesTransactions (
            transaction_id, item, quantity, price_per_unit,
            total_spent, payment_method, location, transaction_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, 
    row['Transaction ID'], 
    row['Item'], 
    int(row['Quantity']), 
    float(row['Price Per Unit']), 
    float(row['Total Spent']), 
    row['Payment Method'], 
    row['Location'], 
    row['Transaction Date'])

# Commit dan tutup koneksi
conn.commit()
cursor.close()
conn.close()

print("✅ Data berhasil dimuat ke SQL Server.")