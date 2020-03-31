# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 10:21
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : DataParam_Handle.py
# @Software: PyCharm
import re
from configparser import NoOptionError

from common.Conf_Handle import ih


class ReplaceData:
    """保存一些要替换的数据"""
    pass


def replace_data(case_data):
    """数据参数格式化"""
    # 匹配规则
    r = "#(.+?)#"
    # 判断匹配结果是否为None
    while re.search(r, case_data):
        # 匹配出第一个要替换的数据
        res = re.search(r, case_data)
        # 提取待替换的内容
        item = res.group()
        # 获取替换内容中的数据项
        key = res.group(1)
        try:
            case_data = case_data.replace(item, ih.get_str("data", key))
        except NoOptionError:
            case_data = case_data.replace(item, str(getattr(ReplaceData, key)))

    return case_data


if __name__ == '__main__':
    data = '{"mobile_phone": "#account#", "pwd": "#pwd#", "reg_name":"#reg_name#"}'
    setattr(ReplaceData, "reg_name", "小明")
    print(replace_data(data))
