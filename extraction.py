import requests #To make API request
import os #To retrieve env variable
from dotenv import load_dotenv

load_dotenv() #Loads env variable from .env file

#Retreiving API key from environment variable
api= os.getenv("api")
if not api:
    raise ValueError("No api key was found")

#Function to extract data from API
def extract_data():
    #Construction of URL to make API request
    city= input("Enter the city name:")
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
    try :
        response= requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("Invalid city name! Please check the name and try again.")
        else:
            print(f"HTTP error occurred: {e}")
    except requests.exceptions.RequestException as e:
           print(f"Data was not fetched: {e}")
           return None

data= extract_data() #Stores fetched data

# Prints the fetched data only when this script is executed
if ( __name__  == "__main__" ):
    print(data)
