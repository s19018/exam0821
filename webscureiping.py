import requests
from bs4 import BeautifulSoup

r = requests.get("https://badminton-navi.net/player/ranking_detail/world/men/single")

soup = BeautifulSoup(r.text, "html.parser")
l=soup.select('a span')

with open("web.txt",mode="w",encoding="utf-8") as f:
    for i in l:
        f.write("{}\n".format(i.getText()))

