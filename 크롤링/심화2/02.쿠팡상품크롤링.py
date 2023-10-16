import requests
from bs4 import BeautifulSoup

path = 'https://www.coupang.com/np/search?q=%EA%B2%8C%EC%9D%B4%EB%B0%8D+%EB%A7%88%EC%9A%B0%EC%8A%A4&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=9&backgroundColor='

# 헤더에 User-Agent, Accept-Language 를 추가하지 않으면 멈춤
header = {
    'Host': 'www.coupang.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
}

response_1 = requests.get(path, headers=header)
html = response_1.text
soup_1 = BeautifulSoup(html, 'html.parser')

links = soup_1.select('a.search-product-link')
    
for link in links:
    sub_path = 'https://www.coupang.com/' + link.attrs['href']
    
    response_2 = requests.get(sub_path, headers=header)
    html = response_2.text
    soup_2 = BeautifulSoup(html, 'html.parser')
    
    # 회사 - 있을 수도 있고, 없을 수도 있음.
    # 중고상품은 태그가 달라짐
    try:
        brand_name = soup_2.select_one('a.prod-brand-name').text
    except:
        brand_name = ""
    # 제품명
    product_name = soup_2.select_one('h2.prod-buy-header__title').text
    # 가격
    product_price = soup_2.select_one('span.total-price > strong').text
    print(brand_name, product_name, product_price)

print('\nDvlp.H.Y.C.Sol\n')