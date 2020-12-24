""" Don't be a bad Son,
 Be the best son using Python

 author: ashraf minhaj
 mail: ashraf_minhaj@yahoo.com
"""

""" install -
$ pip install pandas
$ pip install win10toast
"""

# import libraries
import pandas as pd 
import time
from win10toast import ToastNotifier
from datetime import datetime

# init notifier
toaster = ToastNotifier()

# read the csv file
f = pd.read_csv('medicine_schedule.csv')

# get data from csv file
med_time = f.time

# inside this loop we check for time match
run = True
while run:
	# current time - ct
	ct = datetime.now().strftime("%H:%M")
    
    # try to match it with medicine time
	for t in med_time:
		if t == ct:
		    med_name = f.loc[f['time'] == '06:45', 'name'].iloc[0]
		    toaster.show_toast("Medicine Time",
                   med_name,
                   duration=10)