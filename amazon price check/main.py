""" ** Check Amazon product price and send desktop notification **

Idea: Notify me when my deream smart watch's price drops

author: ashraf minhaj
mail: ashraf_minhaj@yahoo.com
"""

"""
install - 
pip install selenium
pip install beautifulsoup4
pip install win10toast

download chrome web driver from online
Download URL - https://chromedriver.chromium.org/downloads

To get desktop notification you need to active notification from
other senders from the setting menu.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from win10toast import ToastNotifier

driver = webdriver.Chrome('chromedriver.exe')

url = "https://www.amazon.com/Samsung-enhanced-tracking-analysis-coaching/dp/B07VQJDGX2/ref=sxin_10_ac_d_rm?ac_md=1-1-c2Ftc3VuZyBzbWFydCB3YXRjaA%3D%3D-ac_d_rm&crid=L1Z7R7OVGG6F&cv_ct_cx=smart+watch&dchild=1&keywords=smart+watch&pd_rd_i=B07VQJDGX2&pd_rd_r=209af91d-9056-40e2-bac0-419b73781ef4&pd_rd_w=PqCbz&pd_rd_wg=Lxotq&pf_rd_p=116299aa-c459-4c5d-b931-45bc7a073c63&pf_rd_r=29BE2NGYS7WRE47416K0&psc=1&qid=1605553257&sprefix=smart+w%2Caps%2C433&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081"
get = driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

# we know what product we are searching, so we just check the price
price = soup.find('span',id="priceblock_ourprice").text.strip('\n$') # remove dollar sign

# close web driver
driver.quit()

# if price withing my budget range send a notification
if float(price) < 180:
	print("Price within your range boss")
	toaster = ToastNotifier()
	toaster.show_toast("Great News!","Smart Watch price within budget range!!!", duration=50)