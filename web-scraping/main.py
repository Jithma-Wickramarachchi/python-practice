from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/search?q=python&page=20'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')

tags = soup('h3')
for tag in tags:
    print(tag.find('div').text)