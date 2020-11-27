""" get product data from amazon

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
"""

"""
install - 
pip install selenium
pip install beautifulsoup4

download chromeDriver from online
Download URL - https://chromedriver.chromium.org/downloads
"""

from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')


#url = 'https://www.amazon.in/Honor-Watch-Magic-Lava-Black/dp/B07MTKF77H/ref=sr_1_20?crid=1Q152KSCVV4V4&dchild=1&keywords=smart+watch&qid=1605558938&sprefix=smart+wa%2Caps%2C359&sr=8-20'

url = "https://www.amazon.com/Samsung-enhanced-tracking-analysis-coaching/dp/B07VQJDGX2/ref=sxin_10_ac_d_rm?ac_md=1-1-c2Ftc3VuZyBzbWFydCB3YXRjaA%3D%3D-ac_d_rm&crid=L1Z7R7OVGG6F&cv_ct_cx=smart+watch&dchild=1&keywords=smart+watch&pd_rd_i=B07VQJDGX2&pd_rd_r=209af91d-9056-40e2-bac0-419b73781ef4&pd_rd_w=PqCbz&pd_rd_wg=Lxotq&pf_rd_p=116299aa-c459-4c5d-b931-45bc7a073c63&pf_rd_r=29BE2NGYS7WRE47416K0&psc=1&qid=1605553257&sprefix=smart+w%2Caps%2C433&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081"

get = driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html,'html.parser')

price = soup.find('span',id="priceblock_ourprice")
title = soup.find(id="productTitle")

print(title.text.strip('\n'))
print(price.text.strip('\n'))

# close selenium
driver.quit()