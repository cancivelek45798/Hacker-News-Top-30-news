import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
athing_data = soup.find_all(class_="athing")
for data in athing_data:
       print(data.text)
