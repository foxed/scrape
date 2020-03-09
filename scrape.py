from bs4 import BeautifulSoup
import requests

url = "https://www.legendsofamerica.com/we-slang/"

response = requests.get(url)
page = response.text

soup = BeautifulSoup(page, 'html.parser')


last_links = soup.find(class_="clear")
last_links.decompose()

a_slang = soup.find(class_='entry-content')

a_slang_def = a_slang.find_all('p')


for a in a_slang.find_all('a'):
    a.replaceWithChildren()

for aslang in a_slang_def:
    print(a_slang.prettify())

