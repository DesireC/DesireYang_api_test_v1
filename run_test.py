# -*- coding: utf-8 -*-
# @Time    : 2020/3/20 9:27
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : run_test
# @Software: PyCharm

import pytest
from common.Path import REPORTS_DIR
import os
import time

# allure报告存放文件夹
allure_dir = time.strftime("%Y-%m-%d")
# allure测试报告存放路径
allure_path = os.path.join(REPORTS_DIR, allure_dir)
# 生成allure测试报告
pytest.main(["-s", "--alluredir={}".format(allure_path)])
# 把生成的测试报告升级一下(自动执行控制台命令)
os.system("allure generate {} -o {}_2 --clean".format(allure_path, allure_path))
