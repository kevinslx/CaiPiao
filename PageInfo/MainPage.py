# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageInfo.BasePage import BasePage
from PageInfo.LoginPage import LoginPage
from selenium.webdriver.common.action_chains import *


class MainPage(BasePage):
	# 页面元素定位器
	loginbutton_loc = (By.ID, "letvLogin")
	nickname_loc = (By.XPATH, '//*[@id="loginTab"]/div/div[1]/a')
	showhideamount_loc = (By.XPATH, '//*[@id="loginTab"]/div/div[1]/div/div[2]/div/span')
	balancedatamonkey_loc = (By.XPATH, '//*[@id="loginTab"]/div/div[1]/div/div[2]/dl[1]/dd')
	cashdatamonkey_loc = (By.XPATH, '//*[@id="loginTab"]/div/div[1]/div/div[2]/dl[2]/dd')
	lotterydatamonkey_loc = (By.XPATH, '//*[@id="loginTab"]/div/div[1]/div/div[2]/dl[3]/dd')

	# 点击登录触发登陆页面
	def click_loginbutton(self):
		self.find_element(*self.loginbutton_loc).click()

	# 切换页面
	def swith_window(self):
		self.driver.switch_to.window(self.driver.window_handles[0])

	# 定位昵称元素
	def find_nickname(self):
		return self.find_element(*self.nickname_loc)

	#鼠标悬停至昵称处，展示出余额
	def mousemove_to_nickname(self):
		ActionChains(self.driver).move_to_element(self.find_element(*self.nickname_loc)).perform()

	def get_balance(self):
		return self.find_element(*self.balancedatamonkey_loc)

	def get_cash(self):
		return self.find_element(*self.cashdatamonkey_loc)

	def get_lottery(self):
		return self.find_element(*self.lotterydatamonkey_loc)

	def get_show_hide_amount(self):
		return self.find_element(*self.showhideamount_loc)

	def change_show_hide(self):
		self.find_element(*self.showhideamount_loc).click()