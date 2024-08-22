#Main file to examine all the CSV data. 

# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineData():

    def __init__(self):
        self.data = pd.read_csv('./data/fatalities_isr_pse_conflict_2000_to_2023.csv.csv')


    def common_age_deaths(self): 
        pass 