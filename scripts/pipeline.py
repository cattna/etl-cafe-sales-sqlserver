import pandas as pd
import pyodbc
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract(path):
    logging.info("📥 Extracting data from %s", path)
    df = pd.read_excel(path)
    logging.info("✅ Data extracted with %d rows and %d columns", df.shape[0], df.shape[1])
    return df

def transform(df):
    logging.info("🧪 Transforming data (drop duplicate transaction_id)")
    before = df.shape[0]
    df = df.drop_duplicates(subset="Transaction ID")
    after = df.shape[0]
    logging.info("🧹 Removed %d duplicate rows", before - after)
    return df

def load(df, conn_str):
    logging.info("📤 Loading data to SQL Server...")
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    inserted = 0
    skipped = 0

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO SalesTransactions (
                    transaction_id, item, quantity, price_per_unit,
                    total_spent, payment_method, location, transaction_date
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, row['Transaction ID'], row['Item'], row['Quantity'],
                 row['Price Per Unit'], row['Total Spent'], row['Payment Method'],
                 row['Location'], row['Transaction Date'])
            inserted += 1
        except pyodbc.IntegrityError:
            logging.warning("⚠️ Duplicate skipped: %s", row['Transaction ID'])
            skipped += 1

    conn.commit()
    cursor.close()
    conn.close()

    logging.info("✅ Load complete. %d inserted, %d skipped.", inserted, skipped)

def main():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=your_server;"
        "DATABASE=your_database;"
    )

    df = extract(r"D:\github-etlproject\etl-coffee-pipeline-colab\data\clean_data_sales.xlsx")
    df = transform(df)
    load(df, conn_str)

if __name__ == "__main__":
    main()
