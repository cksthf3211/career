from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip
import csv

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬창 안뜨게 함
chrome_options.add_argument('--headless') # headless 모드 활성화
chrome_options.add_argument('--disable-gpu') # GPU 가속 비활성화

# 불필요 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 드라이버 업데이트
serveice = Service(executable_path=ChromeDriverManager().install())

# 옵션 적용
browser = webdriver.Chrome(service=serveice, options=chrome_options)

news = pyautogui.prompt('뉴스기사 입력 >>> ')
print(f'{news} 검색')

# 웹페이지 해당 주소 이동
path = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={news}'

# url 대화
browser.get(path)

# 네이버에서 html 줌
html = browser.page_source

soup = BeautifulSoup(html, 'html.parser')

articles = soup.select("div.info_group") # 뉴스 기사 div 10개 추출

for article in articles:
    links = article.select("a.info")
    if len(links) >= 2: # 링크가 2개 이상이면
        url = links[1].attrs['href'] # 두번째 링크의 href 추출
        
        # 다시 한번 받아옴
        browser.get(url)
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        content = soup.select_one('#dic_area') # 해당 링크 본문의 아이디값 가져옴
        print(content)
        time.sleep(0.7)
        
print('\nDvlp.H.Y.C.Sol\n')