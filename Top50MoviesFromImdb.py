import requests
from bs4 import BeautifulSoup as bs

URL = "https://www.imdb.com/search/title?groups=top_250&sort=user_rating"
r = requests.get(URL)

soup = bs(r.content,'lxml')

lister_list = soup.find('div',class_='lister-list')

for list_item in lister_list.find_all('div',class_='lister-item mode-advanced'):
    content = list_item.find('div',class_='lister-item-content')
    title = content.h3.a.text
    no = content.h3.span.text
    h3 = content.h3
    year = h3.find('span',class_='lister-item-year text-muted unbold')
    rating = content.find('div',class_='inline-block ratings-imdb-rating').strong.text

    print(no,title,year.text,rating)
