import os #To retrieve env variable
import pandas as pd #To manipulate the transformed data as desired
from dotenv import load_dotenv
from sqlalchemy import create_engine #To create connection with the database
from transformation import tred_d #To access the data transformed in tranformation.py

load_dotenv() #Loads env variable from .env file
db_url = os.getenv("db_url")
if not db_url:
    raise ValueError("Database URL not found.")

# Function to load the data into a database
def load(tred_d, db_url, table_name):

    try:
        engine = create_engine(db_url) # Creates connection with database

        tred_d.to_sql(
            name=table_name,
            con=engine,
            if_exists="append",
            index=False
        )# Writes the data into the database

        print(f"Data successfully loaded into table '{table_name}'!")
    except Exception as e:
        print(f"Error loading data to database: {e}")
        print("Exiting the pipeline.")

load(tred_d, db_url, "weather_data")# Loads the data into database
