#Step1: Beginner 1
#Finding all instances of a tag in html at once

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

	print("\n##Now we extract the text behind the p tag\n")
	soup.find_all('p')
	print(soup.find_all('p'))

	soup.find_all('p')[0].get_text()
	print(soup.find_all('p')[0].get_text())


# ##Searching for tags by class and id

	print("\n\n\nNew html page\n")
	page2 = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
	##Print whole html page
	# print(page.content)
	soup = BeautifulSoup(page2.content, 'html.parser')
	# nice looking html page
	print(soup.prettify())

	print("\n##find all p tag where class is outer-text")
	soup.find_all('p', class_='outer-text')
	print(soup.find_all('p', class_='outer-text'))

	# search elements by id
	soup.find_all(id="first")


	# Using CSS selectors
	print("##CSS selectors\n")
	soup.select('div p')
	print(soup.select('div p'))


	print("##New page3 forecast weather")
	page3 = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
	soup = BeautifulSoup(page3.content, 'html.parser')
	
	seven_day = soup.find(id="seven-day-forecast")
	forecast_items = seven_day.find_all(class_="tombstone-container")
	tonight = forecast_items[0]
	print(tonight.prettify())

	period = tonight.find(class_="period-name").get_text()
	short_desc = tonight.find(class_="short-desc").get_text()
	temp = tonight.find(class_="temp").get_text()
	print(period)
	print(short_desc)
	print(temp)

	img = tonight.find("img")
	desc = img['title']
	print(desc)

	# ##Extracting all the information from the page
	print("\n\n##Extract all the information\n")
	period_tags = seven_day.select(".tombstone-container .period-name")
	periods = [pt.get_text() for pt in period_tags]
	print(periods)

	print("\n\n##Getting other data fields\n")
	short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
	temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
	descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

	print(short_descs)
	print(temps)
	print(descs)


# Combining our data into a Pandas Dataframe
	print("\n\n\nCombining panda dataframe\n")
	import pandas as pd
	weather = pd.DataFrame({
	    "period": periods,
	    "short_desc": short_descs,
	    "temp": temps,
	    "desc":descs
	})
	print(weather)


	# Analysis

	# We can now do some analysis on the data. 
	# For example, we can use a regular expression and the Series.str.extract 
	# method to pull out the numeric temperature values:
	temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
	weather["temp_num"] = temp_nums.astype('int')
	print(temp_nums)

	# We could then find the mean of all the high and low temperatures:
	weather["temp_num"].mean()	

	# We could also only select the rows that happen at night:
	is_night = weather["temp"].str.contains("Low")
	weather["is_night"] = is_night
	print(is_night)


finally:
		print("\n\nSuccessfully end the program")