# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 15:36
# @File    : code-1.py
# @Software: PyCharm

import pandas

pd = pandas.read_table('test1.txt',sep=',')
pd1 = pd.loc[pd['姓名']=='小红',:]
pd2 = pd.loc[pd['姓名']=='张明',:]
pd3 = pd.loc[pd['姓名']=='小江',:]
pd4 = pd.loc[pd['姓名']=='小李',:]
print(f"{pd1}\n{pd2}\n{pd3}\n{pd4}")

# 使用正确的列名计算平均成绩
M1 = pd1['成绩'].mean()
M2 = pd2['成绩'].mean()
M3 = pd3['成绩'].mean()
M4 = pd4['成绩'].mean()
print(f"小红的平均成绩:{M1:.2f}")
print(f"张明的平均成绩:{M2:.2f}")
print(f"小江的平均成绩:{M3:.2f}")
print(f"小李的平均成绩:{M4:.2f}")



