# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/18 14:06
# @File    : code-1.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression as LR

# 加载数据
data = pd.read_excel('1.xlsx')
x = data.iloc[:, 1:6]
y = data.iloc[:, 6]

# 创建并拟合线性回归模型
lr = LR()
lr.fit(x, y)
Slr = lr.score(x, y)

# 提取模型系数
c_x = lr.coef_
c_b = lr.intercept_

# 进行预测
x1 = np.array([4, 1.5, 10, 17, 9])
x1 = x1.reshape(1, 5)
R1 = lr.predict(x1)

# 手动计算预测值
r1 = x1 * c_x
R2 = r1.sum() + c_b

# 打印结果
print('x回归系数为：', c_x)
print('回归系数常数项为：', c_b)
print('判定系数为：', Slr)
print('样本预测值为：', R1)

