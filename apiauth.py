import re
import requests

URL = "https://fungover.org/auth/"

jsonbody = {"username": "test2@test.nu","passwo": "passs"}
result = requests.post(URL,json= jsonbody)
if result.status_code != 200:
    print("Error")
print(result.text)