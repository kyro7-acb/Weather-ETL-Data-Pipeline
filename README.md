# Weather ETL Data Pipeline

## Overview
The Weather ETL Data Pipeline is a Python-based project designed to extract weather data for a specified city from the OpenWeatherMap API, transform it into a clean and structured format, and load it into a MySQL database. This pipeline is fully automated, providing an efficient solution for weather data collection and storage.

---

## Features
- Extracts weather data for any city specified by the user.
- Stores processed data into a MySQL database for persistent storage.
- Handles invalid city inputs gracefully with proper error handling.
- Modular design: Separate scripts for extraction, transformation, and loading.
- Raw JSON data is transformed into a tabular format with 9 key attributes:
    - Country Name
    - City Name
    - Humidity
    - Weather Description
    - Temperature (in Celsius)
    - Minimum Temperature (in Celsius)
    - Maximum Temperature (in Celsius)
    - Pressure
    - Date (when the data was fetched)

---

## Technologies Used
- **Python** for scripting and data manipulation.
- **Requests** for making HTTP requests.
- **Pandas** for data transformation.
- **SQLAlchemy** for database connectivity.
- **MySQL** as the database.
- **OpenWeatherMap API** for weather data retrieval.
- **dotenv** for managing environment variables.

---

## Prerequisites

### Tools and Libraries

- **Python 3.8+**
- **MySQL Database**
- **pip (Python Package Installer)**

---

## Setup Instructions
Follow these steps to set up and run the project:

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/kyro7-acb/Weather-ETL-Data-Pipeline.git
```
Navigate to the Weather-ETL-Data-Pipeline folder:
```bash
cd Weather-ETL-Data-Pipeline
```

### 2. Set up a Virtual Environment (Recommended for Dependency Management).
It is recommended to create a virtual environment to keep dependencies isolated:
```bash
python -m venv env
```

### 3. Activate the virtual environment (Only if you create virtual environment).
```bash
# On Windows
.\env\Scripts\activate

# On macOS and Linux
source env/bin/activate
```

### 4. Install the requirements
Create a .env file in the root directory of the cloned project (Weather-ETL-Data-Pipeline/). Add the following environment variables:
```bash
api=<your_openweathermap_api_key>
db_url=mysql+pymysql://<username>:<password>@<host>/<database>
```
#### **Get your API key**:
Get your api key by signing into openweathermap web.
#### **Set Up MySQL Database**:
Create a database named Weather (or your preferred name). Ensure the credentials in db_url match your database setup.

---

## Usage
Run the pipeline by executing the main.py script
```bash
python main.py
```
When prompted, enter the city name to fetch and store its weather data. The data will be loaded into the MySQL database configured in your .env file.

---
## Project Structure
```bash
weather_etl_pipeline/
├── extraction.py        # Extracts data from the OpenWeatherMap API
├── transformation.py    # Transforms raw data into a structured format
├── load.py              # Loads transformed data into MySQL
├── main.py              # Orchestrates the ETL process
├── requirements.txt     # Contains Python dependencies
├── .env                # Environment variables (not included in the repo)
└── README.md           # Project documentation
```

### How It Works

**Extraction**:

Fetches weather data for the specified city from the OpenWeatherMap API using the city name input.

**Transformation**:

Converts JSON data into a Pandas DataFrame.

Extracts and renames the necessary attributes.

Converts temperatures from Kelvin to Celsius.

**Loading**:

Inserts the transformed data into a MySQL table named weather_data.

### Database Structure

The following fields are stored in the MySQL database:

| Field                | Description                    |
|----------------------|--------------------------------|
| Country              | The country of the city        |
| City                 | Name of the city               |
| Humidity             | Humidity percentage            |
| Weather_Description  | A brief description of weather |
| Temperature_C        | Current temperature (°C)       |
| Min_Temperature_C    | Minimum temperature (°C)       |
| Max_Temperature_C    | Maximum temperature (°C)       |
| Pressure             | Atmospheric pressure (hPa)     |
| Date                 | Date when the data was fetched |

### Error Handling
**Invalid API Key**: Ensures an API key is present; otherwise, raises a descriptive error.

**Invalid City Name**: Prompts the user to check the input if the city name is invalid or not found.

**Database Connectivity Issues**: Gracefully handles database connection errors with proper messages.

---

### License
This project is open-source and free to use. Contributions are welcome!
