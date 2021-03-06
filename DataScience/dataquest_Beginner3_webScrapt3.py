# *************************************************************************************************************************
try:
	import pandas as pd
	import requests
	from bs4 import BeautifulSoup

except Exception as e:
	print("Some Modules are missing {}".format(e))

else:
	print("###New page4 forecast weather\n")

	# page4 = requests.get("https://github.com/tishat-ahasan?tab=repositories")
	page4 = requests.get("https://github.com/Sowmik23?tab=repositories")
	soup = BeautifulSoup(page4.content, 'html.parser')
	
	repo_list = soup.find(id="user-repositories-list")
	one_repo = repo_list.find_all(class_="col-12 d-flex width-full py-4 border-bottom public source")

	'''
	# ##Extracting single list elements
	# here one_repo[0],[1],[2],[3] are the repository list
	r = one_repo[0]
	# print(r.prettify())

	# print("\n\nfinding repo name\n\n")
	repo_name = r.find(class_="wb-break-all").get_text()
	repo_des = r.find(class_="col-9 d-inline-block text-gray mb-2 pr-4").get_text()
	language = r.find(class_="ml-0 mr-3").get_text()
	updated_time = r.find(class_="no-wrap").get_text()

	print(repo_name)
	print(repo_des)
	print(language)
	print(updated_time)
	'''

	# ##Extracting all the information from the page
	print("\n\n##Extract all the information\n")
	
	rep = repo_list.select(".col-12 .wb-break-all")
	'''
	names = []
	short_descs = []
	languages = []
	updated_times = []

	for i in rep:
		k = i.get_text()
		print(k)
		if k is None:
			names.append("Null")
		else:
			names.append(k)

	for j in repo_list.select(".col-12 .col-9"):
		k = j.get_text()
		if k is None:
			short_descs.append("Null")
		else:
			short_descs.append(k)

	for k in repo_list.select(".col-12 .ml-0"):
		x = k.get_text()
		print(x)
		if x is None:
			languages.append("Null")
		else:
			languages.append(x)
	print(languages)

	for l in repo_list.select(".col-12 .no-wrap"):
		x = l.get_text()
		if x is None:
			updated_times.append("Null")
		else:
			updated_times.append(x)
			'''

	names = [i.get_text() for i in rep]
	short_descs = [j.get_text() for j in repo_list.select(".col-12 .col-9")]
	languages = [ k.get_text() for k in repo_list.select(".col-12 .ml-0")]
	updated_times = [l.get_text() for l in repo_list.select(".col-12 .no-wrap")]


	# print(names)
	# print(short_descs)
	# print(languages)
	# print(updated_times)

	# languages.append("C++")
	# languages.append("C++")
	# languages.append("C++")


	m = len(names)
	n = len(short_descs)
	o = len(languages)
	p = len(updated_times)

	q = max(m,n)
	q = max(q,o)
	q = max(q,p)

	print(m)
	print(n)
	print(o)
	print(p)

	if q>m:
		for i in range(0, abs(q-m)):
			names.append("Null")

	if q>n:
		for i in range(0, abs(q-n)):
			short_descs.append("Null")

	if q>o:
		for i in range(0, abs(q-o)):
			languages.append("Null")

	if q>p:
		for i in range(0, abs(q-p)):
			updated_times.append("Null")




	# #Combining data into a Pandas Dataframe
	print("\n\n\nCombining panda dataframe\n")


	repositories = pd.DataFrame({
	    "name": names,
	    "short_desc": short_descs,
	    "language": languages,
	    "updated_time": updated_times
	})

	print(repositories)


	# Analysis

	


finally:
		print("\n\nSuccessfully end the program")