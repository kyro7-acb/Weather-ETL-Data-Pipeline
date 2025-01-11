import pandas as pd #To manipulate the extracted data as desired
from extraction import data #To access the data extracted from API
from datetime import datetime #To specify date of the weather information
# Function to Transform data in a neat form
def transform_data(data):
    #Checks if the data is valid or not
    if not data:
        return
    df= pd.json_normalize(data) #Flattens the raw json data

    tred_df = df[["sys.country", "name", "main.temp", "main.humidity","weather","main.temp_min",
                  "main.temp_max", "main.pressure"]].copy()#Selects specific attribute
    tred_df.rename(
        columns={
    "sys.country": "Countrty",
    "name": "City",
    "main.temp": "Temperature (K)",
    "main.humidity": "Humidity",
    "weather": "Weather_Description",
    "main.temp_min": "Minimum Temperature (K)",
    "main.temp_max": "Maximum Temperature (K)",
    "main.pressure": "Pressure",
    "datetime.now().date()": "Date"
    },inplace = True
    )# Renames the column in standard and clear name

    #Converts retrieved temperature's unit from kelvin into celsius
    tred_df["Temperature_C"] = (tred_df["Temperature (K)"] - 273.15).round(2)
    tred_df["Minimum_Temperature_C"] = (tred_df["Minimum Temperature (K)"] - 273.15).round(2)
    tred_df["Maximum_Temperature_C"] = (tred_df["Maximum Temperature (K)"] - 273.15).round(2)

    #Selects specific 'description' attribute
    tred_df["Weather_Description"] = tred_df["Weather_Description"].apply( lambda x: x[0]["description"]
    if isinstance(x, list) and len(x) > 0 else "Unknown")

    #Drops the Temperatures attribute which are in kelvin unit
    tred_df.drop(columns=["Temperature (K)"], inplace= True)
    tred_df.drop(columns=["Minimum Temperature (K)"], inplace= True)
    tred_df.drop(columns=["Maximum Temperature (K)"], inplace= True)

    #Add the current date to the DataFrame
    tred_df["Date"] = datetime.now().date()

    return  tred_df

tred_d=transform_data(data) #Stores the neat and cleaned Transformed data

# Prints the transformed data only when this script is executed
if __name__ == "__main__":
    print(tred_d)
