# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 10:19
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : Path.py
# @Software: PyCharm

import os

BASEDIR = os.path.dirname(os.path.dirname(__file__))

# 配置文件存放路径
CONF_DIR = os.path.join(BASEDIR, "conf")

# 数据存放路径
DATA_DIR = os.path.join(BASEDIR, "data")

# 日志存放路径
LOGS_DIR = os.path.join(BASEDIR, "logs")

# 测试报告存放路径
REPORTS_DIR = os.path.join(BASEDIR, "reports")
