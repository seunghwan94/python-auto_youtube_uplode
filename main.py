from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import chromedriver_autoinstaller
import subprocess
import pyautogui
import pyperclip
import shutil
import time
import os

url='https://studio.youtube.com/channel/UCwRQVYnM_DNokj9Nm2Dib_Q'
id='magolee100'
pw='tlfqj11!'
title = 'test'
folder_path = 'C:\\Users\\MakeBot\\Desktop\\test1\\enAutoShorts\\result'# 동영상 폴더 경로
clickPath = os.getcwd() + '/img/mp4.png'
dragPath = os.getcwd() + '/img/video_up.png'

if os.path.exists(folder_path):
    os.system(f'explorer "{folder_path}"')
else:
    os.mkdir(folder_path)
    os.system(f'explorer "{folder_path}"')

def click_img(imagePath):
    # 이미지 가운데 클릭 (60% 이상 비슷한 이미지면 가운데 클릭)
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = 0.6)
    x, y = location
    pyautogui.click(x, y)

def drag_img(dragImagePath):
    x, y = pyautogui.position()
    # 드래그하여 이미지 저장
    drag_location = pyautogui.locateCenterOnScreen(dragImagePath, confidence = 0.6)
    target_x, target_y = drag_location
    # 이미지 드래그
    pyautogui.mouseDown(x, y)
    pyautogui.dragTo(target_x, target_y,duration=1)
    pyautogui.mouseUp(target_x, target_y)

##########################################################################################################################################
# 구글 드라이브 로그인 이슈로 인한 우회
try:
    shutil.rmtree(r"C:\chrometemp")  # remove Cookie, Cache files
except FileNotFoundError:
    pass

try:
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')  # Open the debugger chrome

except FileNotFoundError:
    subprocess.Popen(r'C:\Users\binsu\AppData\Local\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(service=Service(), options=option)

except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(service=Service(), options=option)

driver.implicitly_wait(10)

driver.get(url=url)
pyautogui.hotkey('alt', 'tab')

pyautogui.write(id)  # Fill in your ID or E-mail
pyautogui.press('tab', presses=3)  # Press the Tab key 3 times
pyautogui.press('enter')
time.sleep(5)
pyautogui.write(pw)
pyautogui.press('enter')

# 가끔 오류생겨 try
try:
    # 유튜브 동영상 업로드
    driver.find_element(By.XPATH, '//*[@id="create-icon"]').click()
    driver.find_element(By.XPATH, '//*[@id="text-item-0"]/ytcp-ve/tp-yt-paper-item-body/div/div/div').click()
except:
    print('pw error 5 sec wait')
    time.sleep(5)
    pyautogui.write(pw)
    pyautogui.press('enter')
    # 유튜브 동영상 업로드
    driver.find_element(By.XPATH, '//*[@id="create-icon"]').click()
    driver.find_element(By.XPATH, '//*[@id="text-item-0"]/ytcp-ve/tp-yt-paper-item-body/div/div/div').click()

##########################################################################################################################################

# mp4.png 이미지 클릭 후 video_up.png 이미지 까지 드래그
click_img(clickPath)
drag_img(dragPath)
time.sleep(1)
# 동영상 재생 종료
pyautogui.hotkey('alt', 'tab')
pyautogui.hotkey('alt', 'f4')
time.sleep(5)
# 제목
pyperclip.copy(title)
pyautogui.hotkey('ctrl', 'v')
# 아동용 아님 체크
driver.find_element(By.XPATH, '//*[@id="audience"]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]').click()

# 다음
driver.find_element(By.XPATH, '//*[@id="next-button"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="next-button"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="next-button"]').click()
time.sleep(2)

# 게시
driver.find_element(By.XPATH, '//*[@id="privacy-radios"]/tp-yt-paper-radio-button[3]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="done-button"]').click()
time.sleep(10)

driver.close()


