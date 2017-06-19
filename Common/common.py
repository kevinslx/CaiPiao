# coding = utf-8
from time import sleep
import unittest


def login(self, username, password):
	self.driver.find_element_by_id("letvLogin").click()
	sleep(1)
	self.driver.switch_to.window(self.driver.window_handles[0])
	self.driver.find_element_by_name("loginname").send_keys(username)
	self.driver.find_element_by_name("password").send_keys(password)
	self.driver.find_element_by_id("sdklogin").click()
	sleep(1)

