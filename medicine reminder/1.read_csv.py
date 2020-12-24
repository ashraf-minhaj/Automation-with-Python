""" Read a csv file using python

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
"""

""" install -
$ pip install pandas
"""

# import library
import pandas as pd 

# read file as pandas dataframe
f = pd.read_csv('medicine_schedule.csv')
print(f)