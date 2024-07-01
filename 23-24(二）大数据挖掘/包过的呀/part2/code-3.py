# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 15:12
# @File    : code-3.py
# @Software: PyCharm

import numpy as np
A = np.mat([[1,2],[3,4]])
B = np.mat([[5,6],[7,8]])
dot = np.dot(A,B)
print(f"矩阵的乘积为：\n{dot}")

A = np.mat([[3,-1],[-1,3]])
A_vaule,A_vector = np.linalg.eig(A)
print(f"特征值：\n{A_vaule} \n特征向量：\n{A_vector}")

A = np.mat([[4,11,14],[8,7,-2]])
Q1, Q2, Q3 = np.linalg.svd(A, full_matrices=False)
print(f"奇异分解：\n{Q1}\n{Q2}\n{Q3}")

D = np.mat([[4,6,8],[4,6,9],[5,6,8]])
DT = np.transpose(D)
print(f"行列式DT为：\n{DT}")
#计算D和DT
D_value = np.linalg.det(D)
DT_value = np.linalg.det(DT)
print(f"D的计算结果为：\n{D_value} \nDT的计算结果为：{DT_value}")