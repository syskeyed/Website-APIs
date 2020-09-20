import requests

json = {"poster":"Your Name Here","syntax":"text","expiration":"","content":"https://github.com/syskeyed"}
r = requests.post('https://paste.ubuntu.com/', data=json)


print(r.status_code)
print(r.text)




