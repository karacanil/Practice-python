#17
from bs4 import BeautifulSoup
import requests

url = 'http://www.nytimes.com'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
headings = soup.findAll("h2", {"class": "story-heading"})

for heading in headings:
    if heading.findAll("a"):
        print(heading.a.text.strip())
    else:
        print(heading.text)
