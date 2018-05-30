# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 15:40:44 2018

@author: Administrator
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from pandas.plotting import scatter_matrix

data = pd.read_csv('C:/Users/Administrator/Desktop/dataset2.csv',encoding='GBK')

font={'family':'SimHei'}
plt.rc('font',**font)

scatter_matrix(data[["百分比利率","抽取用户佣金","金融产品销售额"]],figsize=(10,10),diagonal='kid')

data[["百分比利率","抽取用户佣金","金融产品销售额"]].corr()
x = data[["百分比利率","抽取用户佣金"]]
y = data[["金融产品销售额"]]

#建模
lrModel = LinearRegression()

#训练模型
lrModel.fit(x,y)

#预测
lrModel.predict([[11,50]])

print("评分："+str(lrModel.score(x,y)))
#查看参数
lrModel.coef_

#查看截距
lrModel.intercept_