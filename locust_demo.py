# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 10:25
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : locust_demo.py
# @Software: PyCharm
"""
通过locust进行简单的压力测试
locust -f 编辑的脚本路径+.py文件   --host=链接（你要测试的网站链接）
"""

from locust import HttpLocust, TaskSet, task


# 定义用户行为
class UserBehavior(TaskSet):

    @task
    def baidu_index(self):
        self.client.get("/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000

# os.system("")
