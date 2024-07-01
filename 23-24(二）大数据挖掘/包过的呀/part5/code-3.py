# -*- coding: utf-8 -*-
# @Author  : yueqing
# @Time    : 2024/6/17 8:57
# @File    : code-3.py
# @Software: PyCharm
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
df = pd.read_excel('3.xlsx')

x = df.drop(columns='地区')


pca = PCA(n_components=0.90)
p1 = pca.fit_transform(x)
scaler = StandardScaler()

p1_scaled = scaler.fit_transform(p1)

ex = pca.explained_variance_ratio_
p2 = pd.DataFrame(data=p1_scaled, columns=[f'PC{i+1}' for i in range(p1.shape[1])])
final_df = pd.concat([df['地区'], p2], axis=1)
print("解释的方差比例:", ex)
print("主成成分分析结果：")
print(final_df)

kmeans = KMeans(n_clusters=4, random_state=0, max_iter=500)
kmeans.fit(p1_scaled)
clu = kmeans.labels_
df['Cluster'] = clu
print(df)
