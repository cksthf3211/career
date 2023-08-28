import openpyxl
import random

# 기존 엑셀 파일 불러오기
wb = openpyxl.Workbook()

ws = wb.active

ws.title = 'data'

# 헤더 추가
ws.append(['순번', '제품명', '가격', '수량', '합계'])

# 데이터 추가
name_list = ['기계식 키보드', '게이밍 마우스', '32인치 모니터', '마우스 패드']

for i in range(random.randint(5,10)): # 매출 데이터 (행) 5~10개
    name = random.choice(name_list)
    if name == "기계식 키보드":
        price = 120000
        
    elif name == "게이밍 마우스":
        price = 40000
        
    elif name == "32인치 모니터":
        price = 350000
        
    elif name == "마우스 패드":
        price = 20000
        
    ws.append([i+1, name, price, random.randint(1,5), f'= C{i+2} * D{i+2}'])
    
wb.save("Data/03.엑셀자동화/쇼핑몰.xlsx")