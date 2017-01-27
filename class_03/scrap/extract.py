# import requests
from bs4 import BeautifulSoup as BS

f = open('index.html')
data = f.read()
f.close()

soup = BS(data)
print soup

table = soup.find_all('table')
print len(table)
tab = table[0]

trs = tab.find_all('tr')
print len(trs)

for ix in range(1, len(trs)):
	rows = trs[ix].find_all('td')
	for rx in rows:
		print rx.text,
	print '--------------'