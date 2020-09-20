import requests

json = {"title":"pog","paste":"lmao"}
r = requests.put('https://api.throwbin.io/v1/store', json=json)


print(r.status_code)
print(r.text)