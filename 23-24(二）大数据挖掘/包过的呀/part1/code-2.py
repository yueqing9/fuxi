# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 14:03
# @File    : code-2.py
# @Software: PyCharm

import math

def comput(r, h):
    S = 2 * math.pi * r * r + 2 * math.pi * r * h
    V = math.pi * r * r * h
    return (S , V)
R = comput(10 , 11)
S = R [0]
V = R [1]
print(f"圆柱体的表面积是：{S:.2f} \n圆柱体的体积是：{V:.2f}")

