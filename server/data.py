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

    def deaths_of_people_took_part_in_event(self, year):
        # Filter by year and citizenship first
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        df_filtered_citizenship = df_filtered[df_filtered['citizenship'] == 'Palestinian']
        # Define columns and participation statuses
        columns = ['Participated', 'Count']
        took_part_list = ['Yes', 'No']
        # Collect counts for each participation status
        data = []
        for item in took_part_list:
            count = df_filtered_citizenship[df_filtered_citizenship['took_part_in_the_hostilities'] == item].shape[0]
            data.append([item, count])
        return pd.DataFrame(data, columns=columns)

    def graph_of_common_injury(self, year):
        data = []
        columns = ['Type of Injury', 'Count of Palestinian', 'Count of Israeli']
        data.append(columns)
        df_filtered_by_year = self.data[self.data['date_of_death'].dt.year <= year]
        injuries = ['gunfire', 'stabbing', 'hit by a vehicle', 'explosion', 'physical assault', 
        'shelling', 'being bludgeoned with an axe', 'physically assaulted', 'beating', 
        'stones throwing', 'Strangulation', 'fire', 'house demolition']
        for injury in injuries: 
            df_filtered_palestinian = df_filtered_by_year[df_filtered_by_year['citizenship'] == 'Palestinian']
            df_filtered_israeli = df_filtered_by_year[df_filtered_by_year['citizenship'] == 'Israeli']
            p_count_df = df_filtered_palestinian[df_filtered_palestinian['type_of_injury'] == injury]
            i_count_df = df_filtered_israeli[df_filtered_israeli['type_of_injury'] == injury]
            p_count = len(p_count_df)
            i_count = len(i_count_df)
            data.append([injury, p_count, i_count])
       return data 

    
death_dataset = ExamineData()
print(death_dataset.graph_of_common_injury(2010))


#Ideas: 
#Should look at average age overtime. 