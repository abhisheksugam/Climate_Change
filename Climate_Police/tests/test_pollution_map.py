#run the test with default values of df, state and year 


import unittest
from pollution_map import pollution_map
import pandas as pd


df = pd.read_csv("../data/pollution_us_2000_2016.csv")

source = 'CO' # options: NO2, O3, SO2 and CO
year = '2008' # options: 2000 - 2016
option = 'Mean' # options: Mean, AQI, 1st Max Value

class TestPlot(unittest.TestCase):
  
    def testPlotPollutants(self):
        
		fig, flag = pollution_map(df, source, year, option)
        expected_explanation="Pollution map plotted."
        self.assertTrue(flag, expected_explanation)

if __name__ == '__main__':
    unittest.main()
