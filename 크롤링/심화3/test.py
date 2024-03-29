from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request

import time
import pyautogui
import os

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 크롬창 안뜨게 함
# chrome_options.add_argument('--headless') # headless 모드 활성화
# chrome_options.add_argument('--disable-gpu') # GPU 가속 비활성화

# Mozilla 웹 브라우저에서 온 것처럼 인식 / 자동화된 요청을 감지하고 차단하는 것을 우회
# chrome_options.add_argument("--user-agent=Mozilla/5.0")

# 불필요 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 옵션 적용
browser = webdriver.Chrome(options=chrome_options)
keyword = pyautogui.prompt('검색어를 입력하세요.')

cnt = 0
# 폴더 만들기 (이미 존재하면 += 1)
while True: 
    cnt += 1
    folder_path = f'크롤링/심화3/{keyword}{cnt}모음'
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        break

path = f'https://www.google.com/search?q={keyword}&sca_esv=581612012&tbm=isch&sxsrf=AM9HkKnRu6DCGGz23e29xT4BSB7Hq95zgA:1699754235522&source=lnms&sa=X&ved=2ahUKEwiboaf7rb2CAxWJfd4KHWkWA9MQ_AUoAXoECAQQAw&biw=1552&bih=737&dpr=1.65' # 구글
browser.implicitly_wait(5)
browser.maximize_window()
browser.get(path)

before_h = browser.execute_script("return window.scrollY")

# 무한스크롤
while True:
    time.sleep(2)
    # 맨 아래로 스크롤을 내림
    browser.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)
    
    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")
    
    # 스크롤 높이가 맨 아래와 같다면 무한루프 탈출
    if after_h == before_h:
        break

    # 스크롤 높이 업데이트
    before_h = after_h

imgs = browser.find_elements(By.CSS_SELECTOR, '.rg_i.Q4LuWd')
print(imgs)