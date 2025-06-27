# 🛠️ ETL Cafe Sales Pipeline to SQL Server

An ETL pipeline project to process and load cleaned cafe sales data into SQL Server using Python and Pandas.

---

## 🔄 Pipeline Workflow

This pipeline follows a clear ETL structure:

1. **Extract**  
   - Source data cleaned using Google Colab (`notebook/etl_pipeline.ipynb`)
   - Transformed data is saved as `.xlsx` in `data/`

2. **Transform**  
   - Cleaning includes deduplication, formatting, and revenue calculation (`Total Spent`)
   - Implemented entirely in Colab with Pandas

3. **Load**  
   - Final cleaned data is loaded into a local SQL Server database via `pyodbc`
   - Handled by the script `scripts/pipeline.py`

4. **Visualize (optional)**  
   - A Streamlit dashboard (`scripts/dashboard.py`) visualizes the loaded data
   - Includes total revenue per item, payment method distribution, etc.

---

## 🧰 Tools & Technologies

- Python 3.10+
- Pandas, OpenPyXL, PyODBC
- Google Colab (for data cleaning)
- Microsoft SQL Server
- Streamlit (for optional visualization)

---

## 📁 Project Structure

<pre> ``` etl-cafe-sales-sqlserver/ ├── data/ │ └── clean_data_sales.xlsx ├── notebook/ │ └── etl_pipeline.ipynb ├── scripts/ │ ├── pipeline.py ← main ETL logic │ ├── dashboard.py ← Streamlit dashboard (optional) │ └── run_pipeline.bat ← for local automation ├── sql/ │ └── create_sales_table.sql ├── requirements.txt ├── README.md └── .gitignore ``` </pre>

## ⚙️ Automation (Windows Task Scheduler)

The pipeline is designed to run automatically on a local machine using **Windows Task Scheduler**:

- `scripts/run_pipeline.bat` executes the pipeline
- The ETL process runs end-to-end and loads fresh data into SQL Server
- Can be scheduled daily/weekly based on use case

---

## 📈 Streamlit Dashboard

To visualize the loaded data:

```bash
streamlit run scripts/dashboard.py
You can view:

Total revenue per item

Payment method breakdown

Sales by location

📝 Data Source & Acknowledgments
This project is based on publicly shared datasets and cleaning logic from:

GitHub: WaveKKC/Cafe-Sales-Data-Cleaning

Special thanks to the original author for providing a detailed and open dataset for practice and learning.

🚀 Future Improvements
 Export processed data back to Excel or CSV

 Email notifications on pipeline failure

 Deploy Streamlit dashboard online

 Add logging and exception monitoring

📌 License
This project is intended for educational and portfolio purposes. All data is sample/demo and does not represent real transactions.
