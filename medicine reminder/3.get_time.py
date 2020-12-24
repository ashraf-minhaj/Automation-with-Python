""" get time (hour:mint) 

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
"""
from datetime import datetime

now = datetime.now()

time = now.strftime("%H:%M")
print(time)

# lets check the type of time
print(type(time))

# one liner ct- current time
ct = datetime.now().strftime("%H:%M")
print("one liner:", ct)