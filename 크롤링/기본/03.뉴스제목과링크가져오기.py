import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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


url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"

# 네이버 서버에 대화 시도
driver.get(url)

# load 대기
time.sleep(5)

# 네이버에서 html 줌
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

links = soup.select('.news_tit')

for link in links:
    title = link.text       # 태그 안에 텍스트요소를 가져옴
    url = link.attrs['href']# href의 속성값을 가져옴

    print(title, url)
    
# DevTools listening on ws://127.0.0.1:6373/devtools/browser/e7fbfe73-c3a8-48ea-9061-7f1d414711a5
# [35092:34292:0906/222254.371:ERROR:device_event_log_impl.cc(222)] [22:22:54.371] USB: usb_service_win.cc:415 Could not read device interface GUIDs: 지정된 파일을 찾을 수 없습니다. (0x2)

# 삼성전자, 2Q 파운드리 점유율 증가…TSMC와 격차 줄어 http://www.newsis.com/view/?id=NISX20230905_0002439229&cID=13001&pID=13000
# "삼성전자, 영업익 대폭 상향 전망" http://www.wowtv.co.kr/NewsCenter/News/Read?articleId=A202309060046&t=NN
# 삼성전자, 2분기 파운드리 점유율 11.7%… TSMC와 격차 좁혀 https://biz.chosun.com/it-science/ict/2023/09/05/4ZMM7AFUVVGV5IBDUOPETJ5QCU/?utm_source=naver&utm_medium=original&utm_campaign=biz
# 독일 사로잡은 삼성전자 ‘스마트싱스 에너지’ https://economist.co.kr/article/view/ecn202309050027
# “불황에도 직원 더 뽑았다”…삼성전자, 1년 새 6000명 이상 늘려 https://www.mk.co.kr/article/10822476
# 삼성전자 스마트싱스 에너지, 獨 유력 매체서 '매우 좋음' 등급 https://www.nocutnews.co.kr/news/6006434
# '7만전자' 또 깨졌다…삼성전자, 장중 1%대 하락[특징주] http://www.edaily.co.kr/news/newspath.asp?newsid=02043446635737496  
# Arm, 상장으로 6.5조원 조달 전망...삼성전자 등 10곳 투자 https://view.asiae.co.kr/article/2023090523593344040
# 모교 찾은 경계현 삼성전자 사장 "'스피릿' 느꼈다" 말한 순간 https://www.joongang.co.kr/article/25190205
# "‘9월 효과’ 피하자" 삼성전자 담는 투자자 http://www.fnnews.com/news/202309061819457405