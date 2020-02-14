import requests
response = requests.get("http://www.datasciencecourse.org")
# some relevant fields
response.status_code
response.content # or response.text
response.headers
response.headers['content-type']