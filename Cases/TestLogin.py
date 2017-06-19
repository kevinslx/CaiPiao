#!/usr/bin/env python3
# coding = utf-8
from selenium import webdriver
import time
import unittest
from PageInfo.LoginPage import LoginPage
from PageInfo.MainPage import MainPage
import os

abspath = os.path.abspath('.')


class Login(unittest.TestCase):
	"""测试彩票登录"""
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.url = 'http://cp.lesports.com/'
		self.username = ("13701334231")
		self.password = ("monkeysun")
		self.wrongusername = "1370133423111"

	def test_login_success(self):
		"""测试登录成功"""
		main_page = MainPage(self.driver, self.url)
		main_page.open()
		main_page.click_loginbutton()
		main_page.switch_window()
		login_page = LoginPage(self.driver, self.url)
		login_page.input_username(self.username)
		login_page.input_password(self.password)
		login_page.click_submit()

		if bool(login_page.find_element(*login_page.verifycode_loc)):
			print("请手动输入验证码，并点击再次点击登录按钮")
			time.sleep(5)

		now = time.strftime('%Y-%m-%d_%H_%M_%S')
		self.driver.get_screenshot_as_file(abspath + '\ScreenShot\\' + now + '_login_success.jpg')
		nickname = main_page.find_nickname()
		self.assertTrue("北京乐迷" in nickname.text)

	def test_wrong_username(self):
		"""测试用户名错误登录"""
		main_page = MainPage(self.driver, self.url)
		main_page.open()
		main_page.click_loginbutton()
		main_page.switch_window()
		login_page = LoginPage(self.driver, self.url)
		login_page.input_username(self.wrongusername)
		login_page.input_password(self.password)
		login_page.click_submit()
		now = time.strftime('%Y-%m-%d_%H_%M_%S')
		self.driver.get_screenshot_as_file(abspath + '\ScreenShot\\' + now + '_login_wrong_username.jpg')
		self.assertEqual(login_page.get_error(), "此帐号尚未注册")

	def tearDown(self):
		self.driver.close()


if __name__ == '__main__':
	unittest.main()
