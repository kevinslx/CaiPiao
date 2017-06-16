# coding = utf-8
from time import sleep
import unittest


def login(self, username, password):
	self.browser.find_element_by_id("letvLogin").click()
	sleep(1)
	self.browser.switch_to_window(self.browser.window_handles[0])
	self.browser.find_element_by_name("loginname").send_keys(username)
	self.browser.find_element_by_name("password").send_keys(password)
	self.browser.find_element_by_id("sdklogin").click()
	sleep(1)

