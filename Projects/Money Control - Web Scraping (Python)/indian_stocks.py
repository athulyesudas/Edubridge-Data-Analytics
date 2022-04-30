import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

date = time.strftime("%Y-%m-%d")

baseurl = 'https://www.moneycontrol.com/india/stockpricequote/'

r=requests.get(baseurl)  # output 200 shows that this website is suitable for scraping
r.status_code

headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

productlinks = []

r = requests.get('https://www.moneycontrol.com/india/stockpricequote/')
soup = BeautifulSoup(r.content, 'lxml')
productlist = soup.find_all('td')

for item in productlist:
  for link in item.find_all('a', href=True):
    productlinks.append(baseurl + link['href'])

print(len(productlinks))


print('starting scraping')


stocklist = []

for link in productlinks:
  r = requests.get(link, headers = headers)
  soup = BeautifulSoup(r.content, 'lxml')

  name = soup.find('h1').text.strip()

  current_price = soup.find('div', class_='pcstkspr nsestkcp bsestkcp futstkcp optstkcp').text.strip()

  open = soup.find('td', class_='nseopn bseopn').text.strip()

  previous_close = soup.find('td', class_='nseprvclose bseprvclose').text.strip()

  low = soup.find('td', class_='nseLP bseLP').text.strip()

  high = soup.find('td', class_='nseHP bseHP').text.strip()

  volume = soup.find('td', class_='nsevol bsevol').text.strip()

  value_lacs = soup.find('td', class_='nsevalue bsevalue').text.strip()

  VWAP = soup.find('td', class_='nsevwap bsevwap').text.strip()

  nse_beta = soup.find('span', class_='nsebeta').text.strip()

  bse_beta = soup.find('span', class_='bsebeta').text.strip()

  uc_limit = soup.find('td', class_='nseupper_circuit_limit bseupper_circuit_limit').text.strip()

  lc_limit = soup.find('td', class_='nselower_circuit_limit bselower_circuit_limit').text.strip()

  fiftytwo_week_high = soup.find('td', class_='nseH52 bseH52').text.strip()

  fiftytwo_week_low = soup.find('td', class_='nseL52 bseL52').text.strip()

  ttm_eps = soup.find('td', class_='nseceps bseceps').text.strip()

  ttm_pe = soup.find('td', class_='nsepe bsepe').text.strip()

  sector_pe = soup.find('td', class_='nsesc_ttm bsesc_ttm').text.strip()

  book_value_per_share = soup.find('td', class_='nsebv bsebv').text.strip()

  face_value = soup.find('td', class_='nsefv bsefv').text.strip()

  p_b = soup.find('td', class_='nsepb bsepb').text.strip()

  twentyday_avg_volume = soup.find('td', class_='nsev20a bsev20a').text.strip()

  twentyday_avg_delivery = soup.find('td', class_='nsed20ad bsed20ad').text.strip()

  market_cap = soup.find('td', class_='nsemktcap bsemktcap').text.strip()


  stock = {
    'stock_name': name,
    'date': date,
    'current_price': current_price,
    'open': open,
    'low': low,
    'high': high,
    'volume': volume,
    'market_cap_in_cr': market_cap,
    'previous_close': previous_close,
    'value_in_lacs': value_lacs,
    'VWAP': VWAP,
    'nse_beta': nse_beta,
    'bse_beta': bse_beta,
    'uc_limit': uc_limit,
    'lc_limit': lc_limit,
    '52_week_high': fiftytwo_week_high,
    '52_week_low': fiftytwo_week_low,
    'ttm_eps': ttm_eps,
    'ttm_pe': ttm_pe,
    'sector_pe': sector_pe,
    'book_value_per_share': book_value_per_share,
    'p/b': p_b,
    'face_value': face_value,
    '20_day_avg_volume': twentyday_avg_volume,
    '20_day_avg_delivery': twentyday_avg_delivery
  }

  stocklist.append(stock) 

  print('running') 

print('finished scraping')


df = pd.DataFrame(stocklist)  # saving the data into a dataframe

name = time.strftime("%Y%m%d-%H%M%S")
df.to_csv(name+'.csv', index=False)

