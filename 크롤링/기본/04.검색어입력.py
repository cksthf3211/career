import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()
# 꺼짐 방지 옵션 추가함
chrome_options.add_experimental_option("detach", True)
# 크롬창 안뜨게 함
chrome_options.add_argument('--headless') # headless 모드 활성화
chrome_options.add_argument('--disable-gpu') # GPU 가속 비활성화
# 쓸데없는 오류메세지같은 이상한거 숨기는 코드임
chrome_options.add_argument('--log-level=3')

# C드라이버에 경로 넣지 않아야함
driver = webdriver.Chrome(options=chrome_options)

keyword = input("검색어를 입력하세요  >>>   ")

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + keyword

# 네이버 서버에 대화 시도
driver.get(url)

# load 대기
time.sleep(5)

# 네이버에서 html 줌
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

links = soup.select('.news_tit')

for link in links:
    title = link.text       # 태그 안에 텍스트요소를 가져옴
    url = link.attrs['href']# href의 속성값을 가져옴

    print(title, url)