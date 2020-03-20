from bs4 import BeautifulSoup
import requests
import string

#n = [0,1,2,3,4,5,6,7,8,9]
#i = string.lowercase

#url = "https://www.legendsofamerica.com/we-slang/"
#urls = "https://www.legendsofamerica.com/we-slang/{a}/#{b}".format(a=n, b=i)
urls = ["https://www.legendsofamerica.com/we-slang/#A", "https://www.legendsofamerica.com/we-slang/2/#B","https://www.legendsofamerica.com/we-slang/3/#C","https://www.legendsofamerica.com/we-slang/4/#D","https://www.legendsofamerica.com/we-slang/5/#E","https://www.legendsofamerica.com/we-slang/6/#H","https://www.legendsofamerica.com/we-slang/7/#I","https://www.legendsofamerica.com/we-slang/8/#L","https://www.legendsofamerica.com/we-slang/9/#M","https://www.legendsofamerica.com/we-slang/10/#N","https://www.legendsofamerica.com/we-slang/11/#P","https://www.legendsofamerica.com/we-slang/12/#R","https://www.legendsofamerica.com/we-slang/13/#S","https://www.legendsofamerica.com/we-slang/14/#T","https://www.legendsofamerica.com/we-slang/15/#U"]

# NOW dealing with the issue of the random shit in the <p> tags that aren't definitions being added to the list. was
# like the author's credits. i'm trying to isolate the words/definitions but tis difficult due to the site's layout

for url in urls:
  response = requests.get(url)
  page = response.text
  soup = BeautifulSoup(page, 'html.parser')

  a_slang = soup.find(class_='entry-content')
  words = a_slang.find_all('strong')

  definitions = a_slang.find_all('p')

  for i in definitions:
    list = []

    word = i.text.strip()
    list.append(word)

    print(word)
    
  # definition = i.next_sibling
  #  list.append(definition)

  #  for n in list:
  #    print(n)    

#   for i in definitions:
#    definition = i.text.strip()

#    print(definition)
#    list = []
#    list.append(definition)


   # for n in list:
    #    print(n)


#check if you need this
#last_links = soup.find(class_="clear")
#last_links.decompose()

# a_slang = soup.find(class_='entry-content')

#definitions = a_slang.find_all('p')

#words = a_slang.find_all('strong')

#delete links at top and bottom of page
#for a in a_slang.find_all('a'):
#   a.replaceWithChildren()

#extract the slang entries and their definitions
#for slang in a_slang_def:
 #   print(slang.prettify())

#for i in definitions:
#    print definitions

#for i in words:
#    word = i.text.strip()
#    print word

#for i in definitions:
#    definition = i.text.strip()
#    list = []
#    list.append(definition)
    
#    for n in list:
#        print(n)
