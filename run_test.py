# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 9:27
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : run_test
# @Software: PyCharm

import pytest
from common.Path import ALLURE_DIR, ALLURE_PLUS_DIR, REPORTS_DIR
import os
import time

"""
# log文件的测试报告存放文件名
report_log = os.path.join(REPORTS_DIR, time.strftime("%Y-%m-%d") + '.log')
pytest.main(["-s", f"--result-log={report_log}"])
# xml文件的测试报告存放文件名
report_xml = os.path.join(REPORTS_DIR, time.strftime("%Y-%m-%d") + '.xml')
pytest.main(["-s", f"--junit-xml={report_xml}"])
# html文件的测试报告存放文件名
report_html = os.path.join(REPORTS_DIR, time.strftime("%Y-%m-%d") + '.html')
pytest.main(["-s", f"--html={report_html}"])
"""
# 测试报告存放文件夹
report_file = time.strftime("%Y-%m-%d")
# allure测试报告存放路径
allure_path = os.path.join(ALLURE_DIR, report_file)
# allure-plus测试报告存放路径
allure_plus_path = os.path.join(ALLURE_PLUS_DIR, report_file)

# 生成allure测试报告
pytest.main(["-v", f"--alluredir={allure_path}"])
# 把allure测试报告升级成allure-plus(自动执行控制台命令)
os.system(f"allure generate {allure_path} -o {allure_plus_path} --clean")
