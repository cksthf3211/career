from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

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
chrome_options.add_argument('--headless') # headless 모드 활성화
chrome_options.add_argument('--disable-gpu') # GPU 가속 비활성화

# Mozilla 웹 브라우저에서 온 것처럼 인식 / 자동화된 요청을 감지하고 차단하는 것을 우회
chrome_options.add_argument("--user-agent=Mozilla/5.0")

# 불필요 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 드라이버 업데이트
service = Service(executable_path=ChromeDriverManager().install())

# 옵션 적용
browser = webdriver.Chrome(service=service, options=chrome_options)

# data = ['게이밍+마우스', '기계식+키보드', '27인치+모니터']
# for i in data:
    #print(i)
    #path = f'https://www.coupang.com/np/search?q={i}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={1}&rocketAll=false&searchIndexingToken=1=9&backgroundColor='

path = 'https://www.coupang.com/np/search?q=%EA%B2%8C%EC%9D%B4%EB%B0%8D+%EB%A7%88%EC%9A%B0%EC%8A%A4&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=9&backgroundColor='

# 헤더에 User-Agent, Accept-Language 를 추가하지 않으면 멈춤
header = {
    'Host': 'www.coupang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
}

response_1 = requests.get(path, headers=header)
html = response_1.text
soup_1 = BeautifulSoup(html, 'html.parser')

links = soup_1.select('a.search-product-link')
    
for link in links:
    # 광고상품 제거
    if len(link.select('span.ad-badge-text')) > 0:
        print('광고 상품 입니다.')
    
    sub_path = 'https://www.coupang.com/' + link.attrs['href']
    
    response_2 = requests.get(sub_path, headers=header)
    html = response_2.text
    soup_2 = BeautifulSoup(html, 'html.parser')
    
    # 회사 - 있을 수도 있고, 없을 수도 있음.
    # 중고상품은 태그가 달라짐
    try:
        brand_name = soup_2.select_one('a.prod-brand-name').text
    except:
        brand_name = ""
    # 제품명
    product_name = soup_2.select_one('h2.prod-buy-header__title').text
    # 가격
    product_price = soup_2.select_one('span.total-price > strong').text
    print(brand_name, product_name, product_price)

print('\nDvlp.H.Y.C.Sol\n')