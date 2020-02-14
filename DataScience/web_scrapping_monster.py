import os
import requests
from bs4 import BeautifulSoup

import sys

url = "https://www.monster.com/jobs/search"

Payload = {
	"q": "Python Developer",
	"where": "Bridgeport"
}

headers = {
	"Accept-Encoding": 'gzip, deflate, sdch',
	"Accept-language": 'en-Us, en;q=0.8',
	"User-Agent": 'Mozilla/5.0(Macintosh; Intel, Mac OS X 10 10 ',
	"Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9, image/webp,*/*;q=0.8',
	"Referer": 'http://www.wikipedia.org',
	"Connection": 'keep-alive',
}

r = requests.get(url, headers=headers, params = Payload)
soup = BeautifulSoup(r.text, 'html.parser')


Company = []
Locations = []
Titles = []
Links =[]


for x in soup.findAll("section", class_="card-content"):
	for y in x.findAll("div", class_="summary"):
		company = y.find('div', class_="company")
		location = y.find('div', class_="location")
		title = y.find("h2", class_="title")
		link = y.find('a')
		Links.append(link["href"])

		# print(link["href"])

		Titles.append(title.text)
		Locations.append(location)
		Company.append(company.text)

data = list(zip(Titles, Company, Links, Locations))
print(data)