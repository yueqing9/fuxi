# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 16:38
# @File    : code.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('data.xlsx')
plt.figure(1)
plt.rcParams['font.sans-serif'] = 'SimHei'     # 设置字体为SimHei
plt.plot(range(1,11),df['猪肉价格'].values[:10],'r*--')
plt.plot(range(1,11),df['牛肉价格'].values[:10],'b*--')
# 对横轴和纵轴打上中文标签
plt.xlabel('日期')
plt.ylabel('价格')
#定义图像的标题
plt.title('猪肉和牛肉价格走势图')
#定义两个连续图的区别标签
plt.legend(['猪肉','牛肉'])
plt.xticks(range(1,11,2), df['日期'].values[range(0,10,2)], rotation = 90)

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(range(1,16),df['猪肉价格'].values)
plt.xlabel('日期')
plt.ylabel('价格')
plt.title('猪肉价格走势图')
plt.xticks(range(1,16,2), df['日期'].values[range(0,15,2)], rotation = 90)

plt.subplot(2,1,2)
plt.plot(range(1,16),df['牛肉价格'].values)
plt.xlabel('日期')
plt.ylabel('价格')
plt.title('牛肉价格走势图')
plt.xticks(range(1,16,2), df['日期'].values[range(0,15,2)], rotation = 90)
plt.tight_layout()

# 显示图像
plt.show()