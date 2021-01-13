import requests
from bs4 import BeautifulSoup

url = 'https://www.investing.com/indices/ibovespa-futures'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

resultado =  html.select('.arial_20')
print(resultado)