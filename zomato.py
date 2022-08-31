import requests
from bs4 import BeautifulSoup
import pandas as pd
agent = {"user-Agent":'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}
url = "https://www.zomato.com/hyderabad/mehfil-restaurant-1-nizampet/order"
res = requests.get(url,headers=agent).content
soup = BeautifulSoup(res,'html.parser')
#<h4 class="sc-1s0saks-15 iSmBPS">Grilled Chicken + Chicken Biryani Full</h4>
titles = soup.find_all('h4', class_='sc-1s0saks-15 iSmBPS')
votings = soup.find_all('span',class_='sc-z30xqq-4 hTgtKb')
prices = soup.find_all('span',class_='sc-17hyc2s-1 cCiQWA')
print("Nizampet Mehfil Restaurent Data")
rating = soup.find('div','sc-1q7bklc-1 cILgox')
print('Rating:',rating.text)
l_titles =[]
l_votings = []
l_prices = []
for i,j,k in zip(titles,prices,votings):
    l_titles.append(i.text)
    l_prices.append(j.text)
    l_votings.append(k.text)
Alldata = {'Item':l_titles,'Prices':l_prices,'Votes':l_votings}
df = pd.DataFrame.from_dict(Alldata, orient='index')
df = df.transpose()
print(df)
df.to_csv('Z_mehfildata.csv',index=False)
