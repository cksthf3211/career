import requests
from bs4 import BeautifulSoup

import pyautogui
import openpyxl

keyword = pyautogui.prompt('검색어를 입력하세요.')

wb = openpyxl.Workbook('크롤링/심화2/coupang_result.xlsx')
ws = wb.create_sheet(keyword)
ws.append(['순위', '브랜드명', '상품명', '가격', '상세링크'])
rank = 1
done = False

for page in range(1, 5):
    if done == True:
        break
    
    print(page, "번째 페이지 입니다.")
    path = f'https://www.coupang.com/np/search?q={keyword}&&page={page}'

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
        # 광고상품 제거
        if len(link.select('span.ad-badge-text')) > 0:
            print('광고 상품 입니다.')
            
        sub_path = 'https://www.coupang.com/' + link.attrs['href']
        print(sub_path)
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
        try:
            product_price = soup_2.select_one('span.total-price > strong').text
        except:
            product_price = 0
                
        print(rank, brand_name, product_name, product_price)
        
        ws.append([rank, brand_name, product_name, product_price, sub_path])
        
        rank += 1
        if rank > 100:
            print(f'상품 {rank}개 검색 완료했습니다')
            done = True
            break

wb.save('크롤링/심화2/coupang_result.xlsx')
print('\nDvlp.H.Y.C.Sol\n')