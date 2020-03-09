from bs4 import BeautifulSoup
import requests

URL = 'https://www.legendsofamerica.com/we-slang/'
page = requests.get(URL)