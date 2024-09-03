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

obj = UnderstandCSV()
obj.unique_values_citizenship()