import json
# load json from a REST API call
response = requests.get("https://api.github.com/user",
params={"access_token":token})
data = json.loads(response.content)
json.load(file) # load json from file
json.dumps(obj) # return json string
json.dump(obj, file) # write json to file