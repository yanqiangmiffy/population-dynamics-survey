# !/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@Author:yanqiang 
@File: utils.py 
@Time: 2018/11/23 10:28
@Software: PyCharm 
@Description: 一些通用函数
"""


def year(date):
    date = str(date)
    return int(date[0:4])


def month(date):
    date = str(date)
    return int(date[4:6])


def day(date):
    date = str(date)
    return int(date[6:8])
