import requests
import sys
from bs4 import BeautifulSoup

def search():
	url = 'http://www.wikihow.com/Plan-for-Graduate-School'

	html = requests.get(url).text
	soup = BeautifulSoup(html, "html.parser")

	# descriptions = soup.select('.drop__txt p')
	# title = soup.select('.drop__title a')
	images = soup.select('.whcdn')

	# for line in descriptions:
		# print line

	# for line in title:
	# 	print line

	for image in images:
			src = image.get('src')
			print src

search()