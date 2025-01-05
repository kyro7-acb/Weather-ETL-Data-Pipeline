import requests
import os
from dotenv import load_dotenv

load_dotenv()

#Retreiving api key from environment variable
api= os.getenv("api")
if not api:
    raise ValueError("No api key was found")
#Set the apiendpoint
city= "Kathmandu"
url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"

def extract_data():
    try :
        response= requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
           print(f"Data was not fetched: {e}")
           return None

data= extract_data()
if ( __name__  == "__main__" ):

    print(data)
