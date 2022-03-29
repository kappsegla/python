import requests
import json

URL = "https://api.github.com/repos/kappsegla/library22/releases/latest"

page = requests.get(URL)

dictionary = json.loads(page.text)
print( dictionary['tag_name'])

