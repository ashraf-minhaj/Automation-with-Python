""" Read a csv file using python
    Seperate columns

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

# get time
time = f.time
print(time)

# lets see if we can iterate the values using for loop
for t in time:
	print(t)
#  voila we can!

# type of t?
print(type(t))  # aah we need str to compare, joss