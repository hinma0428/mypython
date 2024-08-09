import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get(r'http://localhost:8888/tree/ch02kmdb/coffeeStore.ipynb')
time.sleep(1)