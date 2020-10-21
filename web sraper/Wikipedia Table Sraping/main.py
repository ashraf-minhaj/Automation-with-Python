""" Python web-scrapper - Get Iphone prices from wikipedia

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
    	#print(data[1].a.text)  # IOS
        #print(data[8].text)    # price

        raw_os = data[1].a.text
        raw_price = data[8].text.split('/') # split prices separated by '/'

        # clean data (remove unnecessary substrings and keep only the version number)
        os = raw_os.replace('iPhone', '').replace('iOS', '').replace('OS', '').replace(' ', '')

        # get first price value, remove dollar sign
        price = raw_price[0].replace('$', '')

        print(f"os: {os} || price: {price}")

        f.write(os+ ','+ price+ "\n") # write values in csv file

    except:     # some None values will come, that's why
        pass    

f.close()  # close to save file