#quotes
from bs4 import BeautifulSoup
import requests

url = 'http://quotes.toscrape.com'
response = requests.get(url).content
sopa = BeautifulSoup(response)
nueva_sopa = sopa.findAll('span', {'class':'text'})

#lista con quotes, se puede limpiar 
text = [i.get_text()for i in nueva_sopa]
print(text)
