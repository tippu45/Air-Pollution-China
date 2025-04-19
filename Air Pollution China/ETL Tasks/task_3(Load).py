import pandas as pd
from sqlalchemy import create_engine

# --- Configuration ---
csv_file_path = "Dataset/processed.csv"
table_name = "Air_Pollution_Data"  # Name of the table in PostgreSQL

# PostgreSQL connection details
db_user = "postgres"
db_password = "2002"
db_host = "localhost"
db_port = "5432"
db_name = "ETL_Pipeline"

# --- Read CSV ---
df = pd.read_csv(csv_file_path)

# --- Create SQLAlchemy Engine ---
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

# --- Write DataFrame to PostgreSQL ---
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f"Data from '{csv_file_path}' successfully loaded into PostgreSQL table '{table_name}'!")
