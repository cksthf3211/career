import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

# 꺼짐 방지 옵션 추가함
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# C드라이버에 경로 넣지 않아야함
driver = webdriver.Chrome(options=chrome_options)

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"

# 네이버 서버에 대화 시도
driver.get(url)

# load 대기
time.sleep(5)

# 네이버에서 html 줌
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

links = soup.select('.news_tit')

print(links)