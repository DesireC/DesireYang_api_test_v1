# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 9:08
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : conftest.py
# @Software: PyCharm
"""
存放 pytest 测试夹具，文件名是固定的
只能放在项目的根目录下，
其他测试模块进行调用的时候不需要进行导入，会自动发现进行使用
"""

import pytest


@pytest.fixture()
def set_up():
    print("在每个用例执行之前执行")
    yield
    print("在每个用例执行之后执行")


@pytest.fixture(scope="class")
def set_up_class():
    print("在测试类执行之前执行")
    yield
    print("在测试类执行之后执行")


# @pytest.fixture(autouse=True)
# def set_up_default():
#     print("默认情况用例执行之前执行")
#     yield
#     print("默认情况用例执行之后执行")
