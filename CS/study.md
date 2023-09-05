# Hi
## requests
- requests는 HTTP 통신을 위한 파이썬 라이브러리 
- GET 요청: 뉴스 보여줘라 서버야 ~
- GET 응답: 여기있어 ~
- POST 요청: 아이디, 비번 줄태니 로그인좀 ~
- POST 응답: 응 비번 틀렸어 ~

## Beautifulsoup
- beautifulsoup는 HTML 분석을 위한 파이썬 라이브러리
- pip install beautifulsoup4

## CSS선택자
- 디자인을 변경 할 HTML 태그를 선택하는 것
    - 크롤링 할 HTML 태그를 선택하는 것

### CSS선택자의 종류
- 태그 선택자
    - 태그의 이름으로 선택한다.
    - 예) h1 a 등
- id 선택자
    - id 값으로 선택한다.
    - 예) #article
- class 선택자
    - class 값으로 선택한다.
    - 예) .info_group
- 자식 선택자
    - 내가 원하는 태그에 별명이 없을 떄 사용
    - 바로 아래에 있는 태그를 선택
    - 예) .logo_sports>span   (해당 클래스 아래의 태그)
    - 예) .new_headline>h4