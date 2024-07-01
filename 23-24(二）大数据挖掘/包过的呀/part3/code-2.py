# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 16:02
# @File    : code-2.py
# @Software: PyCharm

import pandas as pd

df1=pd.read_excel('test2.xlsx')
Nt=df1.iloc[:,[2,3]].values
print(f"数组Nt为：\n{Nt}")

df2=pd.read_excel('test2.xlsx',dtype=str)
TF = (df2['交易日期'].values>='2017-01-05')&(df2['交易日期'].values<='2017-01-16')
print(f"逻辑数组TF为：\n{TF}")

S=sum(Nt[TF,1])
print(f"期间成交量之和为:{S}")