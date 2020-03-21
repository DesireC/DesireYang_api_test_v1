# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 16:03
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : Requests_Handle.py
# @Software: PyCharm
import requests


class RequestsHandle(object):
    """处理request请求"""

    def __init__(self):
        pass


if __name__ == '__main__':
    reports = requests.get("http://apis.juhe.cn/gnyj/query?key=20954fc2c41f31ee67bbd3e208f96008")
    print(reports.json())
