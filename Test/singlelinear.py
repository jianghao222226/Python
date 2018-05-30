# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 13:57:36 2018

@author: Administrator
"""

import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data=pd.read_csv('C:/Users/Administrator/Desktop/dataset1.csv',encoding='GBK')
plt.scatter(data.活动推广费,data.销售额) #散点看趋势，是否符合线性趋势
data.corr()

#估计模型参数，建立回归模型
'''
(1) 首先导入简单线性回归的求解类
LinearRegression
(2) 然后使用该类进行建模，
得到lrModel的模型变量
'''
lrModel=LinearRegression()
#(3) 接着，我们把自变量和因变量选择出来
x=data[['活动推广费']]
y=data[['销售额']]
#模型训练
'''
调用模型的fit方法，对模型进行训练
这个训练过程就是参数求解的过程
并对模型进行拟合
'''
lrModel.fit(x,y)
#对回归模型进行检验
print('线性评分：' + str(lrModel.score(x,y)))
#利用回归模型进行预测
print(lrModel.predict([[60],[70]]))
#查看截距
alpha=lrModel.intercept_[0]
print('alpha :' + str(alpha))
#查看参数
beta=lrModel.coef_[0][0]
print('beta :' + str(beta))
print(alpha+beta*numpy.array([[60],[70]]))