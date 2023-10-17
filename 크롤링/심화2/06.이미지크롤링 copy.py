from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import urllib.request

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment

import time
import pyautogui
import pyperclip
import csv

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬창 안뜨게 함
# chrome_options.add_argument('--headless') # headless 모드 활성화
# chrome_options.add_argument('--disable-gpu') # GPU 가속 비활성화

# Mozilla 웹 브라우저에서 온 것처럼 인식 / 자동화된 요청을 감지하고 차단하는 것을 우회
chrome_options.add_argument("--user-agent=Mozilla/5.0")

# 불필요 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 드라이버 업데이트
service = Service(executable_path=ChromeDriverManager().install())

# 옵션 적용
browser = webdriver.Chrome(service=service, options=chrome_options)

keyword = pyautogui.prompt('검색어를 입력하세요.')

# path = f'https://www.google.co.kr/search?tbm=isch&hl=ko&source=hp&biw=&bih=&q={keyword}' # 구글
path = f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}' # 네이버
browser.implicitly_wait(3)
browser.maximize_window()
browser.get(path)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

# 무한스크롤 시작
while True:
    # 맨 아래로 스크롤을 내림
    time.sleep(2)
    browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)
    
    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    
    # 스크롤 높이가 맨 아래와 같다면 무한루프 탈출
    if after_h == before_h:
        break
    # 스크롤 높이 업데이트
    before_h = after_h

# 이미지 태그 추출
imgs = browser.find_elements(By.CSS_SELECTOR, '._image._listImage')

for i, img in enumerate(imgs, 1):
    # 각 이미지 태그의 주소 추출
    link = img.get_attribute('src')
    print(f'img {i}개: {link}')
    
print('\nDvlp.H.Y.C.Sol\n')