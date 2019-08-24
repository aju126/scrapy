from bs4 import BeautifulSoup
import requests

URL = "https://www.moneycontrol.com/india/stockpricequote/personal-care/hindustanunilever/HU"
def start_parse():
    content = requests.get(URL).content
    soup = BeautifulSoup(content, 'html5lib') 
    title = soup.find('title')
    print(title)

start_parse()
