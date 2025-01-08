import pandas as pd
from extraction import data

def transform_data(data):
    df= pd.json_normalize(data)

    tred_df = df[["sys.country", "name", "main.temp", "main.humidity","weather"]].copy()
    tred_df.rename(
        columns={
    "sys.country": "Countrty",
    "name": "City",
    "main.temp": "Temperature (K)",
    "main.humidity": "Humidity",
    "weather": "Weather_Description"
    },inplace = True
    )
    tred_df["Temperature_C"] = tred_df["Temperature (K)"] - 273.15

    tred_df["Weather_Description"] = tred_df["Weather_Description"].apply( lambda x: x[0]["description"]
    if isinstance(x, list) and len(x) > 0 else "Unknown")

    tred_df.drop(columns=["Temperature (K)"], inplace= True)

    return  tred_df

tred_d=transform_data(data)

if __name__ == "__main__":
    print(tred_d)
