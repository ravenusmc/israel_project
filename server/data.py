#Main file to examine all the CSV data. 

# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineData():

    def __init__(self):
        self.data = pd.read_csv('./data/fatalities_isr_pse_conflict_2000_to_2023.csv')
        # Convert date_of_death to datetime format
        self.data['date_of_death'] = pd.to_datetime(self.data['date_of_death'])

    def average_age_deaths(self, year):
        # Filter data for deaths up to the given year
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        # Group by citizenship and calculate the average age
        avg_age_by_citizenship = df_filtered.groupby('citizenship')['age'].mean()
        return avg_age_by_citizenship

    def deaths_by_group(self, year):
        # Filter data for deaths up to the given year
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        # Group by citizenship and calculate the count
        death_count_by_citizenship = df_filtered.groupby('citizenship')['age'].count()
        return death_count_by_citizenship
    
    def deaths_by_region(self, year):
        # Filter data for deaths up to the given year
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        event_location_region

death_dataset = ExamineData()
# print(death_dataset.average_age_deaths(2010))
print(death_dataset.deaths_by_group(2010))
#Should look at average age overtime. 