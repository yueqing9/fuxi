# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 10:37
# @File    : code-1.py
# @Software: PyCharm

# 创建元组t1和空列表list1
t1 = (1,2,'R','py','Matlab')
list1= []

t = 0
while t < len(t1):
    list1.append(t1[t])
    t = t + 1
# print(list1)
#创建一个空字典dict1
dict1 = {}
Li = ['k',[3,4,5],(1,2,6),18,50]
keys = ['a','b','c','d','e']
for k in range(len(keys)):
    dict1.setdefault(keys[k],Li[k])
# print (dict1)
