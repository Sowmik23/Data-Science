# get all the links within the data science course schedule
from bs4 import BeautifulSoup
import requests
response = requests.get("http://www.datasciencecourse.org/2020")
root = BeautifulSoup(response.content)
root.find("section",id="schedule")\
.find("table").find("tbody").findAll("a")