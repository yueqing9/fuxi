# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/18 14:06
# @File    : code-5.py
# @Software: PyCharm

## 生成布尔值数据表 Data
items = ['西红柿', '排骨', '鸡蛋', '毛巾', '水果刀', '苹果', '茄子', '香蕉', '袜子', '肥皂', '酸奶', '土豆', '鞋子']
import pandas as pd
import numpy as np

data = pd.read_excel('5.xlsx', header=None)
data = data.iloc[:, 1:]
D = dict()
for t in range(len(items)):
    z = np.zeros((len(data)))
    li = list()
    for k in range(len(data.iloc[0, :])):
        s = data.iloc[:, k] == items[t]
        li.extend(list(s[s.values == True].index))
        z[li] = 1
        D.setdefault(items[t], z)
Data = pd.DataFrame(D)  # 布尔值数据表

##（1）小问
# 获取字段名称，并转化为列表
c = list(Data.columns)
c0 = 0.4  # 最小置信度
s0 = 0.2  # 最小支持度
list1 = []  # 预定义列表 list1，用于存放规则
list2 = []  # 预定义列表 list2，用于存放规则的支持度
list3 = []  # 预定义列表 list3，用于存放规则的置信度
for k in range(len(c)):
    for q in range(len(c)):
        # 对第 c[k] 个项目与第 c[q] 个项目挖掘关联规则
        # 规则的前件为 c[k]
        # 规则的后件为 c[q]
        # 要求前件和后件不相等
        if c[k] != c[q]:
            c1 = Data[c[k]]
            c2 = Data[c[q]]
            I1 = c1.values == 1
            I2 = c2.values == 1
            t12 = np.zeros((len(c1)))
            t1 = np.zeros((len(c1)))
            t12[I1 & I2] = 1
            t1[I1] = 1
            sp = sum(t12) / len(c1)  # 支持度
            co = sum(t12) / sum(t1)  # 置信度
            # 取置信度大于等于 c0 的关联规则
            if co >= c0 and sp >= s0:
                list1.append(c[k] + '--' + c[q])
                list2.append(sp)
                list3.append(co)
# 定义字典，用于存放关联规则及其置信度、支持度
R = {'rule': list1, 'support': list2, 'confidence': list3}
# 将字典转化为数据框
R = pd.DataFrame(R)
# 将结果导出 Excel
R.to_excel('r_1.xlsx', index=False)

##（2）小问
import apriori

# 结果文件
outputfile = 'r_2.xlsx'
support = 0.2  # 最小支持度
confidence = 0.4  # 最小置信度
ms = '--'  # 连接符，默认'--'
# 保存结   果到 Excel
apriori.find_rule(Data, support, confidence, ms).to_excel(outputfile)
