# pip install pyautogui
import pyautogui
import time

# 1. 내 컴퓨터 화면의 크기 출력
print(pyautogui.size())
# Size(width=1920, height=1080)

# 2. 마우스 위치 출력
time.sleep(1)
print(pyautogui.position())
# Point(x=888, y=742)

# 3. 마우스 이동
#pyautogui.moveTo(41, 442) # x, y

#pyautogui.moveTo(41, 442, 2) # x, y축으로 2초간 이동

# 4. 마우스 클릭
#pyautogui.click() # 클릭
#pyautogui.click(button='right') # 버튼의 우클릭
#pyautogui.doubleClick() # 더블클릭
#pyautogui.click(clicks=3, interval=1) # 3번 클릭을 1초 간격으로

# 5. 마우스 드래그
# 452,72 -> 801,66 이동 ( 탭 이동 )
pyautogui.moveTo(452,72, 1)
pyautogui.dragTo(801,66, 1)  # x, y축으로 1초간 이동