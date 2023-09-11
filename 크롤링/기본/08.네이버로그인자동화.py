from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

serveice = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=serveice, options=chrome_options)

# 로딩 될 때 까지 5초 기다림
driver.implicitly_wait(5)
# 화면 최대화
driver.maximize_window()
# 웹페이지 해당 주소 이동
path = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
driver.get(path)

# ID입력
id = driver.find_element(By.CSS_SELECTOR, '#id')
id.click()
# id.send_keys('(ID입력)') -> 로봇감지
pyperclip.copy('cksthf3211')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# Password 입력
password = driver.find_element(By.CSS_SELECTOR, '#pw')
password.click()
# password.send_keys('(password입력)') -> 로봇감지
pyperclip.copy('tmxkdlf@11')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, '#log\.login')
login_btn.click()

print('Finish !!')