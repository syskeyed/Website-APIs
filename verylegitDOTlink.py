import requests
import urllib.parse

query = 'https://github.com/syskeyed'
urllib.parse.quote(query)

json = {"long_url":f"{query}"}
r = requests.post('https://verylegit.link/sketchify', data=json)


print(r.status_code)
print(r.text)