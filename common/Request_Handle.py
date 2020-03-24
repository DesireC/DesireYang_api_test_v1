# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 16:03
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : Request_Handle.py
# @Software: PyCharm

"""
=== 发送请求 ===
=== send_requests: 发送HTTP请求
=== RequestsSessionHandle：发送session鉴权的请求
=== send_service：发送webservice请求
"""
import requests
from suds import WebFault
from suds.client import Client


def send_requests(
        url,
        method,
        params=None,
        json=None,
        data=None,
        headers=None):
    """
    发送http请求
    :param url: 请求地址
    :param method: 请求方式
    :param params: get请求参数
    :param json: json请求参数
    :param data: x-www-form-urlencoded格式数据
    :param headers: 请求头
    :return: 响应结果
    """
    # 将大写转化成小写
    method = method.lower()
    methods = {
        'get': requests.get,
        'post': requests.post,
        'patch': requests.patch
    }
    if method in methods:
        return methods[method](
            url=url,
            params=params,
            json=json,
            data=data,
            headers=headers)
    else:
        raise ValueError("请求方式输入有误")


class RequestsSessionHandle(object):
    """发送session鉴权的接口"""

    def __init__(self):
        self.re = requests.session()

    def send(self,
             url,
             method,
             params=None,
             json=None,
             data=None,
             headers=None):
        """
        发送http请求
        :param url: 请求地址
        :param method: 请求方式
        :param params: get请求参数
        :param json: json请求参数
        :param data: x-www-form-urlencoded格式数据
        :param headers: 请求头
        :return: 响应结果
        """
        # 将大写转化成小写
        method = method.lower()
        methods = {
            'get': self.re.get,
            'post': self.re.post,
            'patch': self.re.patch
        }
        if method in methods:
            return methods[method](
                url=url,
                params=params,
                json=json,
                data=data,
                headers=headers)
        else:
            raise ValueError("请求方式输入有误")


def send_service(url_path, interface, data):
    """
    发送WebService请求
    :param url_path: 项目地址
    :param interface: 接口名
    :param data: 参数
    :return: 状态码和信息
    """
    # 创建webservice对象，来调用webservice里面的各类接口
    client = Client(url=url_path)
    try:
        res = eval("client.service.{}({})".format(interface, data))
        result = dict(res)
    except WebFault as e:
        result = dict(e.fault)
    return result


if __name__ == '__main__':
    # reports = requests.get("http://apis.juhe.cn/gnyj/query?key=20954fc2c41f31ee67bbd3e208f96008")
    # print(reports.json())
    rp = send_requests(
        "http://apis.juhe.cn/gnyj/query?key=20954fc2c41f31ee67bbd3e208f96008",
        "patch")
    print(rp.json())
