import pandas as pd
import numpy as np
import folium
import requests

from bs4 import BeautifulSoup

# in : progressBar 구현
from tqdm.notebook import tqdm
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# jupyter nbconvert --to script coffeeStore.ipynb
chrome_options = webdriver.ChromeOptions()  # 크롬 브라우저 옵션
drive_path = 'chromedriver.exe'  # 다운로드 받은 드라이버 파일
myservice = Service(drive_path)  # 드라이버 제어를 위한 서비스 객체
driver = webdriver.Chrome(service=myservice, options=chrome_options)  # 드라이버 객체
print(type(driver))  # 객체가 잘 생성되었는지 확인

wait_time = 10  # 최대 대기 시간
driver.implicitly_wait(wait_time)
<class = selenium.webdriver.chrome.webdriver.WebDriver>


driver.maximize_window()  # 윈도우 창 최대화
# 스타벅스) 매장 찾기-지역 검색 링크 주소
starbucks_url = 'https://www.starbucks.co.kr/store/store_map.do?disp=locale'
driver.get(starbucks_url)  # 해당 페이지로 이동하기
# 스타벅스) '서울' 링크 클릭
starbucks_seoul_selector = '#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a'
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, starbucks_seoul_selector))).click()
# 스타벅스) '서울'-'전체' 클릭
starbuck_seoul_all = '#mCSB_2_container > ul > li:nth-child(1) > a'
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, starbuck_seoul_all))).click()
# 스타벅스 html 코드를 파싱하여 html 파일에 기록합니다.


