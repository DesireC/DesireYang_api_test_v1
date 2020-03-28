# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 11:25
# @Author  : Desire
# @Email   : yangyin1106@163.com
# @Blog    : https://www.cnblogs.com/desireyang/
# @File    : Yaml_Handle
# @Software: PyCharm

import yaml
import os
from common.Path import CONF_DIR


class YamlHandle(object):
    """处理yaml配置文件"""

    def __init__(self, file_name):
        self.file_name = file_name

    def __open(self):
        """
        打开yaml文件，读取全部的信息
        :return: yaml文件中的全部信息
        """
        with open(self.file_name, encoding="utf-8") as f:
            return yaml.load(f, yaml.FullLoader)

    def get_data(self, node):
        """
        读取对应节点的值
        :param node: 节点名称
        :return: 节点对应的值
        """
        return self.__open()[node]


yaml_file = os.path.join(CONF_DIR, 'conf.yaml')
y = YamlHandle(yaml_file)
if __name__ == '__main__':
    data = y.get_data('mysq')
    print(type(data))
