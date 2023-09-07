from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import openpyxl
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

codes = [
    '005930',
    '000660',
    '035720'
]

for code in codes:
    url = f'https://finance.naver.com/item/sise.naver?code={code}'
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    price = soup.select_one('#_nowVal').text #74,000
    price = price.replace(',', '') # 74000
    print(price)
    time.sleep(1)
    
print('크롤링 작업을 마쳤습니다.')