from bs4 import BeautifulSoup
import requests
import time

'''
Crawl the name, category information, price, number of views, address and image link of the item in 58city

'''

info = list() #
# url = 'http://bj.58.com/pbdn/0/'
urls = ['http://bj.58.com/pbdn/0/pn{}/'.format(str(i)) for i in range(1,10)] # Format all target URLs
for url in urls:
    wb_data = requests.get(url) # Get a webpage
    soup = BeautifulSoup(wb_data.text,'lxml') # Parsing HTML code
    links = soup.select('table > tbody > tr > td.t > a[onclick]') # Get a link to each item’s details
    for link in links:
        time.sleep(2) # Limit access frequency
        link_url = link.get('href')
        pro_data = requests.get(link_url)
        pro_soup = BeautifulSoup(pro_data.text,'lxml')
        # Select information
        cls = pro_soup.select('#nav > div > span:nth-of-type(4) > a')[0]
        title = pro_soup.select('div.box_left_top > h1')[0]
        price = pro_soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.info_massege.left > div.price_li > span > i')[0]
        addr = pro_soup.select('div.info_massege.left > div.palce_li > span > i')[0]
        views = pro_soup.select('body > div.content > div > div.box_left > div.info_lubotu.clearfix > div.box_left_top > p > span.look_time')[0]
        data = {
            'cls': list(cls.stripped_strings)[0],
            'title': title.text,
            'price': price.text,
            'addr' : addr.text,
            'views': views.text
        }
        print(data)
        #Save into a list
        info.append(data)

