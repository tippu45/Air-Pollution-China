import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:2002@localhost:3306/etl_pipeline")

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) AS row_count FROM Air_Pollution_Data"))
    row = result.fetchone()
    # print(f"Inserted {row[0]} records into MySQL.")
    print(row[0])