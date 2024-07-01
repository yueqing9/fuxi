# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 14:34
# @File    : code-2.py
# @Software: PyCharm

import numpy as np
N4 = np.load("N4.npy")
print(f"数组N4是：\n{N4}")

N5 = np.array([N4[0][1],N4[0][3],N4[2][0],N4[2][4]])
print(f"二维数组N5是：\n{N5}")

N1 = np.array(N4[0])
N6 = np.hstack((N5,N1))
print(f"二位数组N6是：\n{N6}")