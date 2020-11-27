import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Samsung-enhanced-tracking-analysis-coaching/dp/B07VQJDGX2/ref=sxin_10_ac_d_rm?ac_md=1-1-c2Ftc3VuZyBzbWFydCB3YXRjaA%3D%3D-ac_d_rm&crid=L1Z7R7OVGG6F&cv_ct_cx=smart+watch&dchild=1&keywords=smart+watch&pd_rd_i=B07VQJDGX2&pd_rd_r=209af91d-9056-40e2-bac0-419b73781ef4&pd_rd_w=PqCbz&pd_rd_wg=Lxotq&pf_rd_p=116299aa-c459-4c5d-b931-45bc7a073c63&pf_rd_r=29BE2NGYS7WRE47416K0&psc=1&qid=1605553257&sprefix=smart+w%2Caps%2C433&sr=1-1-12d4272d-8adb-4121-8624-135149aa9081"

# my user agent
u_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

# make a requesst
response = requests.get(URL, headers=u_agent)
print(response)                                # if 200 then successful

data = BeautifulSoup(response.content, 'lxml')
print(data)                                      # print raw data to see

#data = data.prettify()

#prod_data = data.find(id="productTtitle")
#prod_price = data.find(id='priceblock_ourprice')
#print(prod_data)