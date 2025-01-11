from extraction import extract_data #To execute extraction
from transformation import transform_data #To execute transformation
from load import load #To execute loading

# To execute the datapipeline
def main():
    extract_data()
    transform_data()
    load()
