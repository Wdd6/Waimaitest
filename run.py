# -*- coding: utf-8 -*-
"""
@Time    : 2023/10/10 17:53
@Author  : wdd
@File    : run.py
@project : pyproject1
"""
import pytest,os
from tools.handle_yml import get_yml_data
from tools.handle_path import conf_path
if __name__ == '__main__':
    #1- 获取配置文件数据
    res = get_yml_data(f'{conf_path}\config.yml')#字典
    # print(res)
    #2- 调用配置文件执行
    pytest.main(res['runParams'])#res['runParams']  运行参数
    os.system(' '.join(res['reportParams']))#res['reportParams']报告参数
