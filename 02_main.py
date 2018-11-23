# !/usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@Author:yanqiang 
@File: 02_main.py 
@Time: 2018/11/23 10:28
@Software: PyCharm 
@Description:
"""
from utils import *
import pandas as pd
flow_train = pd.read_csv('./input/flow_train.csv')
tran_train = pd.read_csv('./input/transition_train.csv')

flow_train['address'] = flow_train['city_code']+':'+flow_train['district_code']
print(flow_train['address'].value_counts())
