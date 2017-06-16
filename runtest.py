import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import xlrd
import sys, os

# 获取根目录路径
abspath = os.path.abspath('.')
# 添加Cases目录为系统搜索目录，以便根据Excel中勾选的case动态加载相关模块
sys.path.append(abspath + '\Cases')
# 读取Excel，获取相应测试用例信息
excel = xlrd.open_workbook(
	abspath + '\Config\CaseRunner.xlsx')
sheet1 = excel.sheet_by_index(0)        # 获取第一页
module_name = sheet1.col_values(0, 1)   # 获取module名称
class_name = sheet1.col_values(1, 1)    # 获取类名称
case_name = sheet1.col_values(2, 1)     # 获取用例名称
selection = sheet1.col_values(5, 1)     # 获取case选择结果

suite = unittest.TestSuite()


def __add_case(test_module, class_name, case_name):
	if hasattr(test_module, class_name):
		class_instance = getattr(test_module, class_name)
		suite.addTest(class_instance(case_name))
	else:
		raise AttributeError(class_name + '属性不存在')

for i in range(len(selection)):
	if selection[i] == "yes":
		test_module = __import__(module_name[i])
		__add_case(test_module, class_name[i], case_name[i])

if suite.countTestCases() == 0:
	print('未选择测试用例!')
else:
	# 定义报告存放路径及名称
	now = time.strftime("%Y-%m-%d_%H_%M_%S")
	filename = './Report/' + now + 'Result.html'
	fp = open(filename, 'wb')
	runner = HTMLTestRunner(stream=fp, title='彩票测试报告', description='用例执行结果：')
	runner.run(suite)
	fp.close()




