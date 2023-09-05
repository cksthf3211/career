import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com/"

# 네이버 서버에 대화 시도
response = requests.get(url)
# 네이버에서  html 줌
html = response.text

# html 번역선생님으로 수프만듬 / 파싱
soup = BeautifulSoup(html, 'html.parser')

# class 선택자
word = soup.select_one("a.ContentHeaderView-module__tab_text___IuWnG")

# 텍스트 요소만 출력
print(word)