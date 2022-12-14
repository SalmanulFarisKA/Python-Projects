# Work in progress

import re
import requests
from bs4 import BeautifulSoup

req = requests.get("https://iitpkd.ac.in/people/prithvi")

soup = BeautifulSoup(req.content, "html.parser")

req = soup.body

line = print(req.get_text())  # without the title tag

search = re.match('[\w\.-]+@[\w\.-]+', line)

search.groups()
