from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip
import csv

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
# 드라이버 업데이트
serveice = Service(executable_path=ChromeDriverManager().install())
# 옵션 적용
browser = webdriver.Chrome(service=serveice, options=chrome_options)

# 웹페이지 해당 주소 이동
path = 'https://www.naver.com/'
browser.get(path)

# 로딩 될 때 까지 5초 기다림
browser.implicitly_wait(5)
# 화면 최대화
browser.maximize_window()

# 쇼핑 메뉴 클릭
browser.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(4) > a").click()
time.sleep(2)
# 새로운 브라우저 스위칭
browser.switch_to.window(browser.window_handles[1])

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, "#gnb-gnb > div._gnb_header_area_150KE > div > div._gnbLogo_gnb_logo_3eIAf > div > div._gnbSearch_gnb_search_3O1L2 > form > div._gnbSearch_inner_2Zksb > div > input")
search.click()
# 검색어 입력
search.send_keys("아이폰13")
# Keys로 엔터
search.send_keys(Keys.ENTER)

# 스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")
print(f'스크롤 전 높이:{before_h}')

# 무한스크롤
while True:
    # 맨 아래로 스크롤을 내림
    browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)
    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)
    
    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    print(f'스크롤 후 높이:{after_h}')
    
    # 스크롤 높이가 맨 아래와 같다면 무한루프 탈출
    if after_h == before_h:
        break
    
    # 스크롤 높이 업데이트
    before_h = after_h
    
# 파일생성 # r = read, w = write, newline = 줄바꿈x
f = open(r"크롤링/기본/data.csv", 'w', encoding='CP949', newline='')
csvWriter = csv.writer(f)
    
# 상품정보
itmes = browser.find_elements(By.CSS_SELECTOR,".product_info_area__xxCTi")

for item in itmes:
    name = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K").text
    try:        
        price = item.find_element(By.CSS_SELECTOR, ".price_num__S2p_v").text
    except:
        price = '판매중단'
    link = item.find_element(By.CSS_SELECTOR, ".product_title__Mmw2K > a").get_attribute('href')
        
    print(name, price, link)
    # 데이터 쓰기
    csvWriter.writerow([name, price, link])
    
f.close()
print('Finish!!')