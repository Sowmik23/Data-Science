try:
	import requests
	import bs4
except Exception as e:
	print("Some Module are not available {}".format(e))
else:
	res = requests.get('https://facebook.com/')
	print(type(res))
	# res.text
	# print(res.text)

	# now use beautiful soup to beautify you data at the object res.text
	# BeautifulSout('Object that we created', 'how you want to structure your data amon lot of structure as html_parser/lxml/json/csv')

	soup = bs4.BeautifulSoup(res.text, 'lxml')
	print(type(soup))

	x = soup.select('title')
	print(x)
	print(x[0])
	print(x[0].getText())

finally:
	print("\n\nSuccessfully finished running code")