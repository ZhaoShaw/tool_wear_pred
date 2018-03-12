# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:28:25 2018

@author: PC112
"""
import re
import pymysql
import pandas as pd

def addPositonDiff(host,user,password,database,tablename,add_field_name):
    conn=pymysql.connect(host=host,user=user,password=password,db=database)
    try:
        with conn.cursor() as cur:
            sql="alter table %s add %s varchar(255)"%(tablename,add_field_name)
#            cur.execute('alter table %s drop if exists %s'%(tablename,add_field_name))
            cur.execute(sql)
        with conn.cursor() as cur:
            sql="select z_actual_position from %s"%tablename
            cur.execute(sql)
            ret=cur.fetchall()
            diff=calDiff(ret).astype(str)
            print(diff)
            sql='update '+tablename+' set '+add_field_name+'= case'
            for i in range(len(diff)):
                sql+=(" WHEN `id`='%s'"%(i+1)+" THEN '%s'"%diff[i])
            sql+=(' END')
            cur.execute(sql)
        conn.commit()
    finally:
        conn.close()
def calDiff(ret):
    s=pd.Series([i[0] for i in ret]).astype(float)
    s1=pd.Series([0.0])
    for i in range(len(s)-1):
        temp=pd.Series([s.iloc[i+1]-s.iloc[i]])
        s1=pd.concat([s1,temp],ignore_index=True)
    return s1
if __name__ == "__main__":
    host = 'localhost'
    user = 'root'
    password = 'password'
    database = '408data'
    tablename='A01_CCMT060204_EMF_01'
    add_field_name='z_p_diff'
    addPositonDiff(host,user,password,database,tablename,add_field_name)