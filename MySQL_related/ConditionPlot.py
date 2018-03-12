# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:45:08 2018

@author: hasee
"""

import numpy as np
import pandas as pd
import pymysql
import matplotlib.pyplot as plt

def conditionPlot (host,user,password,db,table_1,table_2):
    conn=pymysql.connect(host=host,user=user,password=password,db=db)
    try:
        sql='select time,spindle_torque,spindle_actual_speed,x_p_diff,y_p_diff,z_p_diff from %s'%table_1
        df=pd.read_sql(sql,con=conn,index_col='time').astype(float)
        df.plot(kind='line',figsize=(100,60))
    finally:
        conn.close()
    

if __name__=="__main__":
    host='localhost'
    user='root'
    password='password'
    db='408data'
    table_1='A01_CCMT060204_EMF_01'
    table_2='a01'
    conditionPlot(host,user,password,db,table_1,table_2)