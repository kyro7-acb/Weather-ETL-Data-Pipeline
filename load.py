from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from transformation import tred_d
import os
load_dotenv()
db_Url = os.getenv("db_url")


def load(tred_d, db_url, table_name):

    try:
        engine = create_engine(db_url)

        tred_d.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False
        )
        print(f"Data successfully loaded into table '{table_name}'!")
    except Exception as e:
        print(f"Error loading data to MySQL: {e}")

if __name__ == "__main__":
    load(tred_d, db_Url, "weather_data")
