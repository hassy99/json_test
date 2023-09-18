import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://eiga.com/movie/98389/',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

# ここにコーディングして、metatagを先に持ってきます。
#<meta property="og:title" content="マイ・エレメント : 作品情報 - 映画.com">

#prac
# ogtitle1 = soup.select_one("meta[property='og:title']")
# ogtitle = ogtitle1["content"].split(':')[0]
# print(ogtitle1) #<meta content="マイ・エレメント : 作品情報 - 映画.com" property="og:title"/>
# print(ogtitle) #マイ・エレメント

ogtitle = soup.select_one("meta[property='og:title']")["content"].split(':')[0]
ogimage = soup.select_one("meta[property='og:image']")["content"].split(':')[0]
ogdesc = soup.select_one("meta[property='og:description']")["content"].split(':')[0]

a=[]
a.append(ogtitle)
a.append(ogimage)
a.append(ogdesc)

for i in a:
    print(i)


