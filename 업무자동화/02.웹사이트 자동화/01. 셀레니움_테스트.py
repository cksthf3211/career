# pip install selenium
# 웹 브라우저를 제어할 수 있는 파이썬 라이브러리
# 웹사이트를 자동화할 수 있게 도와줌

# Chrome드라이버 받을 필요 없음!!!!!!!!!!
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 꺼짐 방지 옵션 추가함
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=chrome_options) # C드라이버에 경로 넣지 않아야함

# AttributeError: 'str' object has no attribute 'capabilities' 이 에러는 C드라이버에 경로 넣지 않아야함

driver.get("https://www.naver.com")