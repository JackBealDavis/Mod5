import pandas as pd
import unittest
from eda_v2 import clean
import numpy as np


class TestOperations(unittest.TestCase):

    def setUp(self):
        #test_data = pd.read_csv("03_Library Systembook.csv")
        self.df = pd.read_csv("03_Library Systembook.csv")
        #self.df.drop(16, inplace=True)

    def test_na(self):
        testData_clean = clean(self.df)
        self.assertFalse(testData_clean.isna().any().any(), "NA Values Found")

    #def test_date_duration(self):
        # LOGIC to apply clean() and check that the new col has numbers above 0

    #def test_date_diff(self, colA="Date of entry", ColB="Date of close"):


#class TestOperations(unittest.TestCase):

    #def setUp(self):
        # CREATE A TEST DATAFRAME 
        #data = {
               #'Name': ['Alice', 'Bob', 'Charlie'],
               #'Age': [25, 30, 35],
               #'City': ['London', 'Manchester', 'Birmingham']
               #}

        #df = pd.DataFrame(data)

        #print("DataFrame from dictionary:")
        #print(df)

        # Also create a solution dataframe
    
    # def test_clean_nas(self):
        # RUN your test dataframe through clean() that you imported.

        # do an assertEqual() to check if the output is the same as the solution dataframe (aka it doesn't have nulls)

if __name__ == '__main__':
   unittest.main()



