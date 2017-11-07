#downloading images from web
import random
import urllib
import requests
from bs4 import BeautifulSoup

def download_web_image(url):
	name = random.randrange(1,100)
	#using type cast with str
	full_name="rick"+str(name)+".jpg"
	urllib.urlretrieve(url,full_name)

def spider(max_pages):
		page=1
		while page < max_pages:
                    url='https://wall.alphacoders.com/by_sub_category.php?id=233584&name=Rick+and+Morty+Wallpapers&page=' + str(page)
                    source_code=requests.get(url)
                    plain_text=source_code.text
                    #converting object into a beatiful soup
                    soup = BeautifulSoup(plain_text,"html.parser")
                    #print(soup.prettify())
                    print("Downloading images from "+url)
                    for link in soup.findAll('img'):
                            #to get links
                            href =link.get('src')
                            #print(href)
                            download_web_image(href)

                    page+=1

spider(3)