# This file will be dealing with the CSV file to get ideas from it on what graphs I want to build. 

# importing supporting libraries
import numpy as np
import pandas as pd

class UnderstandCSV():

    def __init__(self):
        self.data = pd.read_csv('./data/fatalities_isr_pse_conflict_2000_to_2023.csv')

    def columns(self):
        print(self.data.columns.tolist())


obj = UnderstandCSV()
obj.columns()