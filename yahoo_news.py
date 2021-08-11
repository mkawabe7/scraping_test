import requests
from bs4 import BeautifulSoup
import re

# スポーツナビのURLにアクセス
URL = "https://sports.yahoo.co.jp/"
rest = requests.get(URL)

# BeautifulSoupにページ内容を読み込ませる
soup = BeautifulSoup(rest.text, "html.parser")

# トップニュースの見出しとURLの情報を取得して出力する
data_list = soup.find_all(class_=re.compile("sn-listPickup__item"))
for data in data_list:
    print(data.a.string.strip())
    print(data.a.attrs["href"])