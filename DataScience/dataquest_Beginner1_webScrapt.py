#Step0: Beginner 0
#Finding an instance of a tag in html

try:
	import requests
	from bs4 import BeautifulSoup

except Exception as e:
	print("Some Modules are missing {}".format(e))

else:
	page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
	##Print whole html page
	# print(page.content)
	soup = BeautifulSoup(page.content, 'html.parser')
	# nice looking html page
	print(soup.prettify())

	print("\n##children print korbe: \n")
	print(list(soup.children))

	print("\n##select children take 3rd item set\n")
	html = list(soup.children)[2]
	list(html.children)
	print(list(html.children))


	print("\n##As we want the text of p tag\n")
	body = list(html.children)[3]
	list(body.children)
	print(list(body.children))

	print("\n##Now we extract the text behind the p tag\n")
	p = list(body.children)[1]
	p.get_text()
	print(p.get_text())







finally:
	print("\n\nSuccessfully end the program")