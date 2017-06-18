# coding = utf-8
from selenium import webdriver
import time
import unittest
import os


class Login(unittest.TestCase):
	def setUp(self):
		cookie_dir = r"C:\Users\sunliangxing\AppData\Local\Google\Chrome\User Data"
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("user-data-dir="+os.path.abspath(cookie_dir))
		self.browser = webdriver.Chrome(chrome_options=chrome_options)
		self.browser.maximize_window()
		test_url = 'http://cp.lesports.com/'

		self.browser.get(test_url)

	def login(self, username, password):
		self.browser.find_element_by_id("letvLogin").click()
		time.sleep(1)
		self.browser.switch_to_window(self.browser.window_handles[0])
		self.browser.find_element_by_name("loginname").send_keys(username)
		self.browser.find_element_by_name("password").send_keys(password)
		self.browser.find_element_by_id("sdklogin").click()

	def test_login_success(self):
		self.login("13701334231", "monkeysun")
		time.sleep(2)
		user = self.browser.find_element_by_xpath('//*[@id="loginTab"]/div/div[1]/a')
		self.browser.get_screenshot_as_file("C:\\Users\\sunliangxing\\PycharmProjects\\Caipiao\\ScreenShot\\login_success.jpg")
		self.assertTrue("北京乐迷" in user.text)

	def test_login_pwd_error(self):
		self.login("13701334231", "monkey")
		time.sleep(2)
		user = self.browser.find_element_by_xpath('//div[@id="login_zh_cn"]/div[2]/div[1]/div[2]/span')
		self.browser.get_screenshot_as_file("C:\\Users\\sunliangxing\\PycharmProjects\\Caipiao\\ScreenShot\\login_pwd_error.jpg")
		self.assertIn("密码不正确", user.text)

	def test_login_username_error(self):
		self.login("13701334231123", "monkeysun")
		time.sleep(2)
		user = self.browser.find_element_by_xpath('//div[@id="login_zh_cn"]/div[2]/div[1]/div[2]/span')
		self.browser.get_screenshot_as_file("C:\\Users\\sunliangxing\\PycharmProjects\\Caipiao\\ScreenShot\\login_username_error.jpg")
		self.assertIn("此帐号尚未注册", user.text)

	def test_login_username_empty(self):
		self.login("", "monkeysun")
		time.sleep(2)
		user = self.browser.find_element_by_xpath('//div[@id="login_zh_cn"]/div[2]/div[1]/div[2]/span')
		self.browser.get_screenshot_as_file("C:\\Users\\sunliangxing\\PycharmProjects\\Caipiao\\ScreenShot\\login_user_empty.jpg")
		self.assertIn("请输入帐号", user.text)

	def test_login_pwd_empty(self):
		self.login("13701334231", "")
		time.sleep(2)
		user = self.browser.find_element_by_xpath('//div[@id="login_zh_cn"]/div[2]/div[1]/div[2]/span')
		self.browser.get_screenshot_as_file("C:\\Users\\sunliangxing\\PycharmProjects\\Caipiao\\ScreenShot\\login_pwd_empty.jpg")
		self.assertIn("请输入密码", user.text)

	def test_logout(self):
		self.login("13701334231", "monkeysun")
		time.sleep(2)
		self.browser.find_element_by_id("letvLogout").click()
		time.sleep(1)
		user = self.browser.find_element_by_id("letvLogin")
		self.browser.get_screenshot_as_file("C:\\Users\\sunliangxing\\PycharmProjects\\Caipiao\\ScreenShot\\logout.jpg")
		self.assertIn("登录", user.text)

	def tearDown(self):
		self.browser.close()


if __name__ == '__main__':
	unittest.main()
