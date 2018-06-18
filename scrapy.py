from bs4 import BeautifulSoup
import requests

page = requests.get("https://dolarhoje.com")
soup = BeautifulSoup(page.content, 'html.parser')
k = soup.find('table').find('tbody').find_all('td')

page2 = requests.get('https://dolarhoje.com/dolar-australiano-hoje/')
soup2 = BeautifulSoup(page2.content, 'html.parser')
k2 = soup2.find('table').find('tbody').find_all('td')

page3 = requests.get('https://dolarhoje.com/dolar-canadense-hoje/')
soup3 = BeautifulSoup(page3.content, 'html.parser')
k3 = soup3.find('table').find('tbody').find_all('td')

page4 = requests.get('https://dolarhoje.com/dolar-neozelandes-hoje/')
soup4 = BeautifulSoup(page4.content, 'html.parser')
k4 = soup4.find('table').find('tbody').find_all('td')

page5 = requests.get('https://dolarhoje.com/euro/')
soup5 = BeautifulSoup(page5.content, 'html.parser')
k5 = soup5.find('table').find('tbody').find_all('td')

page6 = requests.get('https://dolarhoje.com/iene/')
soup6 = BeautifulSoup(page6.content, 'html.parser')
k6 = soup6.find('table').find('tbody').find_all('td')

page7 = requests.get('https://dolarhoje.com/libra-hoje/')
soup7 = BeautifulSoup(page7.content, 'html.parser')
k7 = soup7.find('table').find('tbody').find_all('td')

page8 = requests.get('https://dolarhoje.com/ouro-hoje/')
soup8 = BeautifulSoup(page8.content, 'html.parser')
k8 = soup8.find('table').find('tbody').find_all('td')

page9 = requests.get('https://dolarhoje.com/peso-argentino/')
soup9 = BeautifulSoup(page9.content, 'html.parser')
k9 = soup9.find('table').find('tbody').find_all('td')

page0 = requests.get('https://dolarhoje.com/peso-chileno/')
soup0 = BeautifulSoup(page0.content, 'html.parser')
k0 = soup0.find('table').find('tbody').find_all('td')

pagea = requests.get('https://dolarhoje.com/peso-uruguaio/')
soupa = BeautifulSoup(pagea.content, 'html.parser')
ka = soupa.find('table').find('tbody').find_all('td')

pageb = requests.get('https://dolarhoje.com/won-sul-coreano-hoje/') 
soupb = BeautifulSoup(pageb.content, 'html.parser')
kb = soupb.find('table').find('tbody').find_all('td')

pagec = requests.get('https://dolarhoje.com/yuan-hoje/')
soupc = BeautifulSoup(pagec.content, 'html.parser')
kc = soupc.find('table').find('tbody').find_all('td')

url = requests.get('https://api.coinmarketcap.com/v2/ticker/?convert=BRL').json()
upd = url['data']['1']['last_updated']