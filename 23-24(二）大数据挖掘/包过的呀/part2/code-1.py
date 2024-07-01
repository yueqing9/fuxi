# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 14:23
# @File    : code-1.py
# @Software: PyCharm

import numpy as np

list1 = [1,2,4,6,7,8]
tup1 = (1,2,3,4,5,6)
N1 = np.array(list1)
print(f"数组N1是：\n{N1}")
N2 = np.array(tup1)
print(f"数组N2是：\n{N2}")
N3 = np.ones((1,6))
print(f"数组N3是：\n{N3}")
N4 = np.vstack((N1,N2,N3))
print(f"二维数组N4是：\n{N4}")
np.save('N4',N4)