import os
import sys
from selenium import webdriver
import time

url = 'http://cp.lesports.com'
cookie_dir = r"C:\Users\sunliangxing\AppData\Local\Google\Chrome\User Data"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir="+os.path.abspath(cookie_dir))
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.get(url)

cookie = driver.get_cookies()

driver.find_element_by_id("letvLogin").click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_name("loginname").send_keys('13701334231')
driver.find_element_by_name("password").send_keys('monkeysun')
driver.find_element_by_id("sdklogin").click()


time.sleep(5)

driver.quit()

