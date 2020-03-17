from bs4 import BeautifulSoup
import requests

url = "https://www.legendsofamerica.com/we-slang/"

response = requests.get(url)
page = response.text

soup = BeautifulSoup(page, 'html.parser')

#check if you need this
#last_links = soup.find(class_="clear")
#last_links.decompose()

a_slang = soup.find(class_='entry-content')

definitions = a_slang.find_all('p')

words = a_slang.find_all('strong')

#delete links at top and bottom of page
for a in a_slang.find_all('a'):
    a.replaceWithChildren()

#extract the slang entries and their definitions
#for slang in a_slang_def:
 #   print(slang.prettify())

#for i in definitions:
#    print definitions

#for i in words:
#    word = i.text.strip()
#    print word

for i in definitions:
    definition = i.text.strip()
    list = []
    list.append(definition)
    print(list)
