try:
	import requests
	from bs4 import BeautifulSoup
	import pandas as pd 
except Exception as e:
	print("Some Modules are missing {}".format(e))
else:
	url = "https://github.com/tishat-ahasan?tab=repositories"
	r = requests.get(url)
	soup = BeautifulSoup(r.text, 'html.parser')

	li = soup.findAll('div', class_='d-inline-block mb-1')
	base_url = "https://github.com/"

	no = []
	Repo = []
	url = []

	for x,i in enumerate(li):
		for a in i.findAll('a'):
			newUrl = base_url + a["href"]
		no.append(x)
		Repo.append(i.text.strip())
		url.append(newUrl)
		# print(x, i.text.strip(), newUrl)
	temp = list(zip(no, Repo, url ))
	df = pd.DataFrame(data=temp, columns=["No", "Repositories", "Url"])
	print(df)
	# print(df.to_html)  to save it just add .to_excel/.to_json etc.

finally:
	print("\n\nSuccessfully end the program")