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
pyperclip.copy('c')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
# pw.send_keys('dasdsad')
pyperclip.copy('t')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 로그인 버튼, 클릭
driver.find_element(By.CSS_SELECTOR, "#log\.login").click() # 객체 / 클릭
time.sleep(1)

# 로그인 후 메일함으로 이동
driver.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(1) > a").click()
time.sleep(1)

# 새로운 텝으로 전환 ( 스위칭 )
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)

# 메일 쓰기 클릭
driver.find_element(By.CSS_SELECTOR, "#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write").click()
time.sleep(1)

# 받는사람 입력
receive = driver.find_element(By.CSS_SELECTOR, "#recipient_input_element")
receive.click()
pyperclip.copy('cksthf3211@naver.com')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 제목 입력
title = driver.find_element(By.CSS_SELECTOR, "#subject_title")
title.click()
pyperclip.copy('셀레니움 메일 자동화 테스트')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)


# 내용 입력 + iframe 접근해야함
content = driver.find_element(By.CSS_SELECTOR, "#content > div.contents_area > div > div.editor_area > div > div.editor_body > iframe")
content.click()
pyperclip.copy('셀레니움 메일 자동화 테스트 내용입니다. 완성입니다. 셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.셀레니움 메일 자동화 테스트 내용입니다. 완성입니다.')
pyautogui.hotkey('ctrl', 'v')
# 엔터
pyautogui.press('enter')
pyautogui.press('enter')
# 다시 입력
pyperclip.copy('복붙을 하자 복붙을 하자 복붙을 하자 복붙을 하자')
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 보내기
driver.find_element(By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task").click()
time.sleep(1)

# 창 닫기
driver.close()
time.sleep(1)

# 원래 창 닫기
driver.switch_to.window(driver.window_handles[0])
driver.close()

print("Success!!")