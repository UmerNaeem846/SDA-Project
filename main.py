import os
print("Current working directory:", os.getcwd())
config_path = os.path.join(os.path.dirname(__file__), "config.json")

import json
from data_loader import gdb_data
from data_processor import (
    data_conversion,
    clean_data,
    region_filter,
    year_filter,
    country_filter
)
from statistics import average_gdp_region, sum_gdp_region
from dashboard import show_dashboard

#functions
def load_config(path):
    
    #Load configuration from a JSON file.
    try:
        with open(path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception("Configuration file not found")
    except json.JSONDecodeError:
        raise Exception("Invalid JSON format in config file")

def validate_config(config):

    #Validate required fields in the configuration.
    required_fields = ["region", "year", "operation", "output"]
    for field in required_fields:
        if field not in config:
            raise Exception(f"Missing configuration field: {field}")

    if config["operation"] not in ["average", "sum"]:
        raise Exception("Operation must be 'average' or 'sum'")

    if not isinstance(config["year"], int):
        raise Exception("Year must be an integer")

    if config["output"] != "dashboard":
        raise Exception("Only 'dashboard' output is supported in Phase 1")


def main():
    
    #Load and validate configuration
    config = load_config(config_path)
    validate_config(config)

    #Load raw CSV/Excel data
    raw_data = gdb_data("data/gdp_with_continent_filled.xlsx") #To be checked again...Take a look at it

    #Convert to standard format
    converted_data = data_conversion(raw_data)

    #Clean data (remove rows with missing GDP)
    cleaned_data = clean_data(converted_data)

    #Apply filters
    filtered_data = region_filter(cleaned_data, config["region"])
    filtered_data = year_filter(filtered_data, config["year"])
    if "country" in config:
        filtered_data = country_filter(filtered_data, config["country"])

    if not filtered_data:
        raise Exception("No data found for the selected configuration")

    #Perform statistical operation
    if config["operation"] == "average":
        result = average_gdp_region(filtered_data)
    else:
        result = sum_gdp_region(filtered_data)

    #Show results on dashboard
    show_dashboard(config, filtered_data, result)


if __name__ == "__main__":
    main()
