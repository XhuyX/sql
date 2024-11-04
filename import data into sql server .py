# nhớ tải thêm packer pyodbc
import pandas as pd
from sqlalchemy import create_engine

# File path to your data file
file_path = r"C:\Users\Dell5090\Downloads\BaiThucHanh_03 - MOBILE Cards.csv"  # Update with your file name

# Load data into a pandas DataFrame
df = pd.read_csv(file_path)  # Or pd.read_excel(file_path) for Excel files

# SQL Server connection details
server = '.'  # Local server
database = 'CardPaymentDB'
table_name = 'CardStore'  # Target SQL table

# Create a connection to SQL Server using Windows Authentication
conn_string = f'mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
engine = create_engine(conn_string)

# Import the data into SQL Server
try:
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
    print("Data imported successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
