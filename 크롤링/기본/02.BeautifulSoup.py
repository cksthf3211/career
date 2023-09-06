from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

# 꺼짐 방지 옵션 추가함
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# C드라이버에 경로 넣지 않아야함
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.naver.com/"

# 네이버 서버에 대화 시도
driver.get(url)

# load 대기
time.sleep(5)

# 네이버에서 html 줌
html = driver.page_source

# html 번역선생님으로 수프만듬 / 파싱
soup = BeautifulSoup(html, 'html.parser')

# class 선택자
word = soup.select_one("a.ContentHeaderView-module__tab_text___IuWnG")

# 텍스트 요소만 출력
print(word.text)