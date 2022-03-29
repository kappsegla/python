import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,"html.parser")

jobs = soup.findAll("h2",class_="title is-5")

for job in jobs:
    print(job.text)