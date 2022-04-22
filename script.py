import sys
import pandas as pd
import numpy as np
import argparse
import json

global data
data = pd.read_csv('covid-cases.csv', low_memory=False)

class CovidCase():
    """
    This is the simple class we will be using to perform parse functions.

    """

    def __init__(self, date, country):
        """
        Initialize the class by settingg up the some features.
        """
        print(data[data.country == 'Peru']['cases'].sum())
        self.date = date
        self.country = country
        self.cases= 0
        self.deaths = 0

    def parse_country(self, country):
        """
        Perform parsing on some input.
        """
        try:
            country = country.lstrip().rstrip()
            country = country.capitalize()
            return country
        except (ValueError, TypeError):
            print("Parsing Error.")
    
    def convert_date(self, string):
        format = '%d/%m/%Y'
        try:
            return datetime.strptime(string, format)
        except (ValueError, TypeError):
            print("Parsing Error.")
    
    
    def convert_to_json(self):
        
        value = {
        "country": self.country,
        "date": self.date,
        "report": 
            {
                "cases": self.get_cases(),
                "deaths": self.get_deaths()
            }
        }
        
        try:
            
            return json.dumps(value)
        except (ValueError, TypeError):
            print("Parsing Error.")

    def get_cases(self):
        return data[data.country == self.country]['cases'].sum()
    
    def get_deaths(self):
        return data[data.country == self.country]['deaths'].sum()
           
        
def main():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--country', action="store")
        parser.add_argument('--date', action="store")

        args = parser.parse_args()
        case = CovidCase(args.date, args.country)
        print(case.convert_to_json())

    except:
        print('Error!')
        sys.exit()


if __name__ == "__main__":
    main()