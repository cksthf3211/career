# Hi
## requests
- requests는 HTTP 통신을 위한 파이썬 라이브러리 
- GET 요청: 뉴스 보여줘라 서버야 ~
- GET 응답: 여기있어 ~
- POST 요청: 아이디, 비번 줄태니 로그인좀 ~
- POST 응답: 응 비번 틀렸어 ~

### requests의 한계
- 로그인이 필요한 사이트 어려움 (세션처리)
- 동적으로 HTML을 만드는 경우 어려움

#### 동적으로 HTML을 만드는 경우
- 스크롤 하거나 클릭하면 데이터가 생성됨
- URL 주소가 변경되지 않았는데 데이터가 변함
- 표, 테이블 형태의 데이터

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

## 셀레니움 이란?
- 웹 어플리케이션 테스트를 위한 도구
- 브라우저를 실제로 띄워서 사람처럼 동작하도록 만들 수 있음.

### 무한스크롤 처리 방법
- 현재 스크롤된 높이를 알 수 있는 자바스크립트 명령어 입력
- window.scrollY

## 워드 클라우드란?
- 중요 단어를 더 잘 보이게 만드는 기법
![Alt text](../assets/image.png)