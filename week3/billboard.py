#
# ビルボードTOP100を表示する
# 2023/09/08 hasui
#
import requests
from bs4 import BeautifulSoup

#init
URL = "https://www.billboard-japan.com/charts/detail?a=hot100"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#Scrape
musics = soup.select("#content2 > div > div.leftBox > table > tbody > tr")

#リスト表示
for music in musics:
    #TOP100リストの中にバナーの要素が含まれている判定
    flg  = music.select_one(".exbanner")

    if flg is None:
        # 要素がバナーでない場合は情報を取得する
        rank  = music.select_one("td > span").text
        artist  = music.select_one("p.artist_name").text.strip()
        title = music.select_one("p.musuc_title").text.strip()

        #アウトプット
        print(rank,artist,title)

    else:
        #要素がバナーの場合何もしない
        pass

print("**end**")


