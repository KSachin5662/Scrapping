from turtle import title
import requests
from bs4 import BeautifulSoup
import pandas as pd
agent = {"user-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
url = "https://www.swiggy.com/restaurants/mehfil-nizampet-x-road-kukatpally-hyderabad-56096"
res = requests.get(url,headers=agent).content
soup = BeautifulSoup(res,'html.parser')
r = soup.find_all('div', class_='_2l3H5' )
v = soup.find('span','_1iYuU')
title = soup.find_all('h3',class_='styles_itemNameText__3ZmZZ')
l_titles = []
for i in title:
    l_titles.append(i.text)
price = soup.find_all('span',class_='rupee')
l_price = []
for i in price:
    l_price.append('₹'+i.text)
Alldata = {'Item':l_titles,"Prices":l_price}
df = pd.DataFrame.from_dict(Alldata, orient='index')
df = df.transpose()
print('Nizampet Mehfil Restaurent Data')
print('Rating:',r[0].text,'(',v.text,')')
print(df)
df.to_csv('S_mehfildata.csv',index=False)
