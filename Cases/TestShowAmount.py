# coding = utf-8
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import *
from Common.common import *
from PageInfo.MainPage import MainPage
from PageInfo.LoginPage import LoginPage
import os

abspath = os.path.abspath('.')


class ShowAmount(unittest.TestCase):
	"""测试金额显示"""
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.url = 'http://cp.lesports.com/'
		self.username = ("13701334231")
		self.password = ("monkeysun")

	def test_showamount(self):
		"""测试金额明文及暗纹显示"""
		main_page = MainPage(self.driver, self.url)
		main_page.open()
		#登录
		main_page.login(self.username,self.password)
		#鼠标悬停
		main_page.mousemove_to_nickname()
		now = time.strftime('%Y-%m-%d_%H_%M_%S')
		self.driver.get_screenshot_as_file(abspath + '\ScreenShot\\' + now + '_暗文数据.jpg')
		#默认个人数据显示暗文
		self.assertEqual('＊＊＊＊＊＊＊', main_page.get_balance().text)
		self.assertEqual('＊＊＊＊＊＊＊', main_page.get_cash().text)
		self.assertEqual('＊＊＊＊＊＊＊', main_page.get_lottery().text)
		self.assertEqual('显示金额', main_page.get_show_hide_amount().text)
		print("暗文显示数据为："+main_page.get_balance().text)
		#再次悬停后点击切换为明文数据
		main_page.mousemove_to_nickname()
		main_page.change_show_hide()
		self.driver.get_screenshot_as_file(abspath + '\ScreenShot\\' + now + '_明文数据.jpg')
		#查看个人数据改为明文
		self.assertNotEqual('＊＊＊＊＊＊＊', main_page.get_balance().text)
		self.assertNotEqual('＊＊＊＊＊＊＊', main_page.get_cash().text)
		self.assertNotEqual('＊＊＊＊＊＊＊', main_page.get_lottery().text)
		self.assertEqual('隐藏金额', main_page.get_show_hide_amount().text)
		print("明文显示数据为："+main_page.get_balance().text)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()