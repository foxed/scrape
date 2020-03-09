from bs4 import BeautifulSoup
import requests

url = "https://www.legendsofamerica.com/we-slang/"

response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'lxml')

tags = soup.find_all('a')

for tag in tags:
    print(tag.get('href'))
