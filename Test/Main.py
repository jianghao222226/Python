# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 16:26:32 2018

@author: Administrator
"""
import numpy as np
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns

conn = pymysql.connect(host='10.219.56.141',user='root',password='micronix14!',db='masmec_2ndxl3assembly',charset='latin1')
sql = 'SELECT t100.vPRESS5 AS t100_pressifit_max_load,t50.vLIFT7 AS t50_load_to_exit_W9,t50.vLIFT9 AS t50_load_to_exit_W0,t70.vPIANTAGGIO_1 AS t70_pressfit_load_out,t70.vPiantaggio_3 AS t70_pressfit_max_out FROM X3L2A100 t100 INNER JOIN X3L2A050 t50 ON t100.`partid` = t50.`partid` INNER JOIN X3L2A070 t70 ON t100.`partid` = t70.`partid` WHERE t100.sonplasfailure = 24 AND t50.`sonplasfailure`=0 AND t70.`sonplasfailure`=0'
df = pd.read_sql(sql,con=conn,columns=('t100_pressifit_max_load','t50_load_to_exit_W9','t50_load_to_exit_W0','t70_pressfit_load_out','t70_pressfit_max_out'))
df_t50_load_to_exit_W9=df[(df.t50_load_to_exit_W9<1000000) & (df.t100_pressifit_max_load<1000000)]
df_t50_load_to_exit_W0=df[(df.t50_load_to_exit_W0<1000000) & (df.t100_pressifit_max_load<1000000)]
df_t70_pressfit_load_out=df[(df.t70_pressfit_load_out>0) & (df.t100_pressifit_max_load<1000000)]
df_t70_pressfit_max_out=df[(df.t70_pressfit_max_out>0) & (df.t100_pressifit_max_load<1000000)]
with sns.axes_style('white'):
    sns.jointplot(x='t50_load_to_exit_W9',y='t100_pressifit_max_load',data=df_t50_load_to_exit_W9,kind='hex',color='k',size=(8))
    sns.jointplot(x='t50_load_to_exit_W0',y='t100_pressifit_max_load',data=df_t50_load_to_exit_W0,kind='hex',color='k',size=(8))
    sns.jointplot(x='t70_pressfit_load_out',y='t100_pressifit_max_load',data=df_t70_pressfit_load_out,kind='hex',color='k',size=(8))
    sns.jointplot(x='t70_pressfit_max_out',y='t100_pressifit_max_load',data=df_t70_pressfit_max_out,kind='hex',color='k',size=(8))
    #sns.regplot(x='t50_load_to_exit_W9', y='t100_pressifit_max_load', data=dfFilter) #回归
conn.close()
print('OK')