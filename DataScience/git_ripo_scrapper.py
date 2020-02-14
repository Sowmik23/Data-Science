try:
	import requests
	from bs4 import BeautifulSoup
except Exception as e:
	print("Some Modules are missing {}".format(e))
else:
	url = "https://github.com/tishat-ahasan?tab=repositories"
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	li = soup.findAll('div', class_='d-inline-block mb-1')
	base_url = "https://github.com/"

	for x,i in enumerate(li):
		for a in i.findAll('a'):
			newUrl = base_url + a["href"]
		print(x, i.text.strip(), newUrl)
finally:
	print("\n\nSuccessfully end the program")