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
        death_count_by_region = df_filtered.groupby('event_location_region')['age'].count()
        return death_count_by_region
    
    # I need to break this down by selected group - Israeli's and Palestinians 
    def deaths_of_people_took_part_in_event(self, year):
        # Filter data for deaths up to the given year
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        df_filtered_citizenship = df_filtered[df_filtered['citizenship'] == 'Palestinian']
        print(df_filtered_citizenship)
        input()
        # deaths_by_taken_part = df_filtered.groupby('took_part_in_the_hostilities').count()
        return deaths_by_taken_part
        
#[nan, 'No', 'Yes', 'Unknown', 'Israelis', 'Object of targeted killing']#
death_dataset = ExamineData()
print(death_dataset.deaths_of_people_took_part_in_event(2020))
#Should look at average age overtime. 