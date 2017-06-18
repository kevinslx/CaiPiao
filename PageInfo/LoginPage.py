# coding = utf-8
from selenium.webdriver.common.by import By
from PageInfo.BasePage import BasePage


class LoginPage(BasePage):
	# 页面元素定位器
	username_loc = (By.NAME, "loginname")
	password_loc = (By.NAME, "password")
	submit_loc = (By.ID, "sdklogin")
	loginerror_loc = (By.XPATH, '//*[@id="login_zh_cn"]/div[2]/div[1]/div[2]/span')
	verifycode_loc = (By.NAME, 'regcode')

	# 输入用户名
	def input_username(self, username):
		self.find_element(*self.username_loc).send_keys(username)

	# 输入密码
	def input_password(self, password):
		self.find_element(*self.password_loc).send_keys(password)

	# 点击登录按钮
	def click_submit(self):
		self.find_element(*self.submit_loc).click()

	# 取得登录错误提示信息
	def get_error(self):
		return self.find_element(*self.loginerror_loc).text
