from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyperclip
import pyautogui

# 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=chrome_options) # C드라이버에 경로 넣지 않아야함
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
# 브라우저 창 최대화
driver.maximize_window()

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
# 입력기능
# id.send_keys('saddsad') 이 방식은 기계가 했다고 오해를 하기 때문에 아래와 같은 방식으로 접근
pyperclip.copy('sfdsfsdfsdf')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
# pw.send_keys('dasdsad')
pyperclip.copy('1212121')
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼, 클릭
driver.find_element(By.CSS_SELECTOR, "#log\.login").click() # 객체 / 클릭
