# coding: UTF-8
import requests
from bs4 import BeautifulSoup
import re

html = requests.get("http://aoc.s602.xrea.com/")
soup = BeautifulSoup(html.content, "html.parser")

ul = soup.div.find_all("ul", attrs={"class" : "live-channels"})
live_list = []
for l in ul:
    for li in l.select("li"):
        live_list.append({
            "link"          : li.span.find("a").get("href"),
            "thumbnail"     : li.span.a.find("img").get("src"),
            "user"          : li.find("span", attrs={"class" : "user"}).a.text,
            "viewers"       : li.find("span", attrs={"class" : "viewers"}).text.strip(),
            "status"        : li.find("span", attrs={"class" : "status"}).text.strip(),
            "showtime"      : li.find("span", attrs={"class" : "showtime"}).text.strip()
        })

#結果吐き出し JSONで吐き出される
print(live_list)