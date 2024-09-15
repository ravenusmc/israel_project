# This file will be dealing with the CSV file to get ideas from it on what graphs I want to build. 

# importing supporting libraries
import numpy as np
import pandas as pd

class UnderstandCSV():

    def __init__(self):
        self.data = pd.read_csv('./data/fatalities_isr_pse_conflict_2000_to_2023.csv')

    def columns(self):
        print(self.data.columns.tolist())

    def unique_values_took_part_in_the_hostilities(self):
        print(self.data['took_part_in_the_hostilities'].unique().tolist())
        #[nan, 'No', 'Yes', 'Unknown', 'Israelis', 'Object of targeted killing']#
    
    def unique_values_for_common_injuries(self):
        print(self.data['type_of_injury'].unique().tolist())
        # ['gunfire', 'stabbing', 'hit by a vehicle', 'explosion', 'physical assault', 
        # 'shelling', 'being bludgeoned with an axe', 'physically assaulted', 'beating', 
        # 'stones throwing', 'Strangulation', nan, 'fire', 'house demolition']
    
    def unique_values_citizenship(self): 
        print(self.data['citizenship'].unique().tolist())
        ['Palestinian', 'Israeli', 'Jordanian', 'American']

    def unique_ammunition(self):
        print(self.data['ammunition'].unique().tolist())
        # ['live ammunition', 'missile', 'rocket', '0.22-caliber bullets', 'bomb', 
        #  'knife', 'shell', 'rock', 'rubber-coated metal bullets', 'stun grenade', 
        #  'teargas canister', 'flare bomb', 'sponge rounds', 'mortar fire', 'grad rocket', 
        #  'flechette shells', 'phosphorus shell', 'Qassam rocket', 'explosive belt', 
        #  'grenade', 'car bomb']
    
    def unique_killed_by(self):
        print(self.data['killed_by'].unique().tolist())
        ['Israeli security forces', 'Palestinian civilians', 'Israeli civilians']
    
    def min_year_value(self): 
        print(self.data['date_of_event'].min())
        # Min Year is 2000
    
    def max_year_value(self):
        print(self.data['date_of_event'].max())
        # Max Year is 2023

obj = UnderstandCSV()
obj.max_year_value()