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
        citizen_type = ['American', 'Israeli', 'Jordanian', 'Palestinian']
        average_age_data = []
        # Filter data for deaths up to the given year
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        # Group by citizenship and calculate the average age
        avg_age_by_citizenship = df_filtered.groupby('citizenship')['age'].mean().apply(np.ceil)
        count = 0
        for citizen in citizen_type:
            if citizen in avg_age_by_citizenship.index:  # Check if citizen exists in the group
                average_age_data.append([citizen, avg_age_by_citizenship[citizen].item()])
            else:
                average_age_data.append([citizen, None])
            count += 1
        # Sort the list, treating None as the lowest value
        average_age_data.sort(key=lambda x: (x[1] is None, x[1]), reverse=True)
        # print(average_age_data)
        return average_age_data

    def deaths_by_group(self, year):
        citizen_type = ['American', 'Israeli', 'Jordanian', 'Palestinian']
        death_by_nationality = []
        # Filter data for deaths up to the given year
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        # Group by citizenship and calculate the count
        death_count_by_citizenship = df_filtered.groupby('citizenship')['age'].count()
        for citizen in citizen_type:
            if citizen in death_count_by_citizenship.index: 
                death_by_nationality.append([citizen, death_count_by_citizenship[citizen].item()])
            else: 
                death_by_nationality.append([citizen, None])
        # Sort the list, treating None as the lowest value
        death_by_nationality.sort(key=lambda x: (x[1] is None, x[1]), reverse=True)
        return death_by_nationality

    
    def deaths_by_region(self, year):
        regions = ['Gaza Strip', 'Israel', 'West Bank']
        deaths_by_region = []
        # Filter data for deaths up to the given year
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        death_count_by_region = df_filtered.groupby('event_location_region')['age'].count()
        for region in regions: 
            if region in death_count_by_region.index: 
                deaths_by_region.append([region, death_count_by_region[region].item()])
            else: 
                deaths_by_region.append([region, None])
        deaths_by_region.sort(key=lambda x: (x[1] is None, x[1]), reverse=True)
        # print(deaths_by_region)
        return deaths_by_region

    def deaths_of_people_took_part_in_event(self, year):
        # Filter by year and citizenship first
        df_filtered = self.data[self.data['date_of_death'].dt.year <= year]
        df_filtered_citizenship = df_filtered[df_filtered['citizenship'] == 'Palestinian']
        # Define columns and participation statuses
        columns = ['Participated', 'Count']
        took_part_list = ['Yes', 'No']
        # Collect counts for each participation status
        took_part_in_event = []
        for item in took_part_list:
            count = df_filtered_citizenship[df_filtered_citizenship['took_part_in_the_hostilities'] == item].shape[0]
            took_part_in_event.append([item, count])
        return took_part_in_event

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
        # print(data)
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
        return data 

    def average_age_of_killed_by_year(self, year):
        pass
    

    
# death_dataset = ExamineData()
# print(death_dataset.graph_of_common_injury(2023))


