import requests
from bs4 import BeautifulSoup as BS

# url = 'https://techcrunch.com/'

# r = requests.get(url)
#html = r.text

html = open('index.html').read()

soup = BS(html)

ul = soup.find_all('ul', id='river1')[0]
lis = ul.find_all('h2')

print len(lis)
for ix in range(len(lis)):
	print ix, lis[ix].find_all('a')[0]['href']