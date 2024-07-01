# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/18 14:06
# @File    : code-2.py
# @Software: PyCharm

import pandas as pd

data = pd.read_excel('2.xlsx')
x_train=data.iloc[:20,1:4]
y_train=data.iloc[:20,4]
x_test=data.iloc[20:,1:4]

from sklearn.linear_model import LogisticRegression as LR
clf = LR()
clf.fit(x_train, y_train)
rv=clf.score(x_train, y_train)
R=clf.predict(x_test)
print('逻辑回归模型拟合准确率： ',rv)
print('逻辑回归模型评估结果： ',R)

from sklearn import svm
clf = svm.SVC(kernel='rbf')
clf.fit(x_train, y_train)
rv=clf.score(x_train, y_train)
R=clf.predict(x_test)
print('支持向量机模型拟合准确率： ',rv)
print('支持向量机评估结果： ',R)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5,2), random_state=1)
clf.fit(x_train, y_train)
rv=clf.score(x_train, y_train)
R=clf.predict(x_test)
print('神经网络模型拟合准确率： ',rv)
print('神经网络评估结果： ',R)
