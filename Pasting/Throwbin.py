import requests

json = {"title":"Example Title","paste":"Paste Content"}
r = requests.put('https://api.throwbin.io/v1/store', json=json)


print(r.status_code)
print(r.text)
