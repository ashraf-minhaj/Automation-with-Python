""" Python web-scrapper - 
* Get Iphone prices by iOS from wikipedia
 and save in a CSV file * 

install -
$ pip install bs4

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
"""

import requests
from bs4 import BeautifulSoup

URL="https://en.wikipedia.org/wiki/IPhone"

res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')

# open if exists else create file
f = open('downloaded_data.csv', 'a')  # append mode
f.write("OS,Price\n")

for items in soup.find('table', class_='wikitable').find_all('tr')[1::1]:
    data = items.find_all(['th','td'])
    #print(data)
    
    try:
        # clean data (remove unnecessary substrings and keep only the version number)
        os = data[1].a.text.replace('iPhone', '').replace('iOS', '').replace('OS', '').replace(' ', '')

        # split prices separated by '/', get first price value, remove dollar sign
        price = data[8].text.split('/')[0].replace('$', '') 

        print(f"os: {os} || price: {price}")
        f.write(os+ ','+ price+ "\n") # write values in csv file

    except:     # some None values will come, that's why
        pass    

f.close()  # close to save file