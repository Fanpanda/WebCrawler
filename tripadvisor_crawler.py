import requests
from bs4 import BeautifulSoup
import time

"""

Crawl the name, classification information and image link of the tripadvisor

"""

# url = "https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html"

urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#FILTERED_LIST'.format(str(i)) for i in range(0,1200,30)] # Format all target URLs

#------------------------------------------------------Crawl the information in single URL--------------------------------------------------------
def Trip_crawler(url,data=None):
    wb_data = requests.get(url) # Get a webpage
    time.sleep(4) # Limit access frequency
    soup = BeautifulSoup(wb_data.text, 'lxml') # Parsing HTML code
	# Select information
    titles = soup.select('div.listing_title > a[target="_blank"]')
    imgs = soup.select("img[width=180]")
    cates = soup.select('div.listing_info > div.tag_line > div')
    for i in range(len(cates)):
        if len(cates[i].text) <= 1:
            cates[i] = 'None'
    while 'None' in cates:
        cates.remove('None')

    for title, img, cate in zip(titles, imgs, cates):
	# Save the obtained information in a dictionary
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings)

        }
        print(data)

if __name__ =="__main__":
    for url in urls:
        Trip_crawler(url)
  

