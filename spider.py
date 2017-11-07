import requests
from bs4 import BeautifulSoup


def spider(max_pages):
		page=1
		while page < max_pages:
                    url='https://stackoverflow.com/questions?page=' + str(page)+'&sort=frequent'
                    source_code=requests.get(url)
                    plain_text=source_code.text
                    #converting object into a beatiful soup
                    soup = BeautifulSoup(plain_text,"html.parser")
                    for link in soup.findAll('a',{'class':'question-hyperlink'}):
                            #to get links
                            href = 'https://stackoverflow.com'+link.get('href')
                            #to download html content
                            title=link.string
                            print(href+"  "+title)
                            get_single_item_data(href);


                    page+=1

def get_single_item_data(item_url):
    source_code = requests.get(item_url).text

    # converting object into a beatiful soup
    soup = BeautifulSoup(source_code,"html.parser")
    #for item_name in soup.findAll('a', {'class':'comment-user'}):
           #print(item_name.string)
    for link in soup.findAll('a',{'class':'comment-user'}):
            href='https://stackoverflow.com'+link.get('href')
            print(href)

spider(2)
		     
