import requests
r = requests.get('https://api.github.com/',auth = ('',''))
print(r.status_code)
print(r.headers['content-type'])


token = "" # not going to tell you mine
response = requests.get("https://api.github.com/user",
params={"4d464318c3d30e76772250a0c165acc392b4b9fb":token})
print(response.content)


