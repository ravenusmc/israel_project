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
        columns = ['Type of Injury', 'Palestinian Count', 'Israeli Count']
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
        print(data)
        return data 
    
    def common_ammunition_used(self, year):
        columns = ['Type of Ammunition', 'Palestinian Count', 'Israeli Count']
        data = [columns]
        
        # Filter data by the given year and citizenship
        df_filtered_by_year = self.data[self.data['date_of_death'].dt.year <= year]
        df_palestinian = df_filtered_by_year[df_filtered_by_year['citizenship'] == 'Palestinian']
        df_israeli = df_filtered_by_year[df_filtered_by_year['citizenship'] == 'Israeli']

        type_of_ammunition = ['live ammunition', 'missile', 'rocket', '0.22-caliber bullets', 'bomb', 
                            'knife', 'shell', 'rock', 'rubber-coated metal bullets', 'stun grenade', 
                            'teargas canister', 'flare bomb', 'sponge rounds', 'mortar fire', 
                            'grad rocket', 'flechette shells', 'phosphorus shell', 'Qassam rocket', 
                            'explosive belt', 'grenade', 'car bomb']
        
        for ammo in type_of_ammunition:
            # Count occurrences for each type of ammunition
            p_count = df_palestinian[df_palestinian['ammunition'] == ammo].shape[0]
            i_count = df_israeli[df_israeli['ammunition'] == ammo].shape[0]
            data.append([ammo, p_count, i_count])
        print(data)
        return data
    
    # I think that for this graph I want to filter by Israeli and Palestinian and then 
    # see count of who was killed. 
    def what_killed_individual(self, year):
        columns = ['Killed by', 'Palestinian Count', 'Israeli Count']
        data = [columns]
        df_filtered_by_year = self.data[self.data['date_of_death'].dt.year <= year]
        df_palestinian = df_filtered_by_year[df_filtered_by_year['citizenship'] == 'Palestinian']
        df_israeli = df_filtered_by_year[df_filtered_by_year['citizenship'] == 'Israeli']
        killed_by_list = ['Israeli security forces', 'Palestinian civilians', 'Israeli civilians']
        for kill_by in killed_by_list:
            p_count = df_palestinian[df_palestinian['killed_by'] == kill_by].shape[0]
            i_count = df_israeli[df_israeli['killed_by'] == kill_by].shape[0]
            data.append([kill_by, p_count, i_count])
        print(data)

    
death_dataset = ExamineData()
print(death_dataset.what_killed_individual(2020))


