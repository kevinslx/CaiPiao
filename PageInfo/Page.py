import os
import sys
from selenium import webdriver

path = os.path.abspath('..')
filename = path + '\Config\config.ini'

file = open(filename, 'r')
print(file.readline())
print('again')
print(file.readline())
file.close()

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')







