# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/18 14:06
# @File    : code-4.py
# @Software: PyCharm

import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor as MP

# 1.数据获取
data = pd.read_excel('4.xlsx')

x_train = data.iloc[:, 1:4]
y_train = data.iloc[:, 4:6]

clf = MP(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=8, random_state=1)
clf.fit(x_train, y_train);

a = np.array([[73.39, 3.9635, 0.9880], [75.55, 4.0975, 1.0268]])  # 预测2010和2011年
y1 = clf.predict(a)
y1 = pd.DataFrame(y1)

s = [2010, 2012]
s = pd.DataFrame(s)

yy = pd.concat([s, y1], axis=1)
yy.columns = ['时间', '公路客流量', '公路货运量']
print(yy)
