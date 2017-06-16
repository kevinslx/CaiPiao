# coding = utf-8
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
	def __init__(self, selenium_driver, base_url):
		self.driver = selenium_driver
		self.base_url = base_url

	def open(self):
		self.driver.maximize_window()
		self.driver.get(self.base_url)

	def find_element(self, *loc):
		try:
			WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element(*loc).is_displayed())
			return self.driver.find_element(*loc)
		except:
			print("%s 页面中未能找到 %s 元素" %(self, loc))

