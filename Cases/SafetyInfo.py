# coding = utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import *
from Common.common import *


class Safety(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.maximize_window()
		test_url = 'http://cp.lesports.com/'
		self.browser.get(test_url)

	def tearDown(self):
		self.browser.close()

	def test_show_noinfo(self):
		#登录
		login(self, "13701334231", "monkeysun")
		#点击进入个人中心
		self.browser.find_element_by_id("individual").click()
		#检查UI显示绑定及认证信息
		data1 = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div[3]/a[1]')
		data2 = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div[3]/a[2]')
		data3 = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div[3]/a[3]')
		data4 = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/div[3]/a[4]')
		self.browser.get_screenshot_as_file("C:\\Users\\sunliangxing\\PycharmProjects\\Caipiao\\ScreenShot\\未绑定信息.jpg")
		self.assertEqual('未绑定', data1.text)
		self.assertEqual('未认证', data2.text)
		self.assertEqual('未绑定', data3.text)
		self.assertEqual('未认证', data4.text)
		#进入安全信息检查绑定及认证信息
		#time.sleep(2)
		self.browser.find_element_by_xpath('//*[@id="userAuth"]/dd[1]/a').click()
		data1 = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[1]/div[2]/dl/dt/span')
		data2 = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/dl/dt/span')
		data3 = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/dl/dt/span')
		data4 = self.browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[4]/div[2]/dl/dt/span')
		self.browser.get_screenshot_as_file("C:\\Users\\sunliangxing\\PycharmProjects\\Caipiao\\ScreenShot\\安全信息页未绑定信息.jpg")
		self.assertEqual('未绑定', data1.text)
		self.assertEqual('未认证', data2.text)
		self.assertEqual('未绑定', data3.text)
		self.assertEqual('未认证', data4.text)
		


if __name__ == '__main__':
	unittest.main()