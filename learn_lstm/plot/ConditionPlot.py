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
        feedrate=[]
        komat_id=[]
        l=[]
        feedrate,komat_id=findKomatid(conn,table_2,experimental_group_1)
        rec_len=recLen(conn,komat_id)
#        s=0
#        for i in range(len(rec_len)):
#            s=s+rec_len[i][0]
#        print(s)
        for i in range(len(feedrate)):
            l=l+[feedrate[i]]*rec_len[i][0]
        feed_con=pd.DataFrame(data=l,index=df.index,columns=['feed_rate'],dtype=np.float64)
        df1=pd.concat([df,feed_con],axis=1)
        df1.plot(kind='line',figsize=(100,60))
    finally:
        conn.close()
def findKomatid(conn,table_2,experimental_group_1):
    with conn.cursor() as cur:
        sql="select komat_id from %s"%table_2+" where experimental_group regexp '^.*%s' order by experimental_group ASC,original_no ASC"%experimental_group_1
        cur.execute(sql)
        ret=cur.fetchall()
        temp_1=[]
        temp_2=[]
        for i in range(len(ret)):
            if ret[i][0]=='None':
                continue
            else:
                sql_1="select feed_rate from %s where komat_id = '%s'"%(table_2,ret[i][0])
                cur.execute(sql_1)
                ret_1=cur.fetchall()
                temp_1.append(ret_1[0][0])
                sql_2="SELECT * FROM information_schema.tables WHERE table_name regexp '^%s'"%ret[i][0]
                cur.execute(sql_2)
                ret_2=cur.fetchall()
                temp_2.append(ret_2[0][2])
    return temp_1,temp_2

def recLen(conn,komat_id):
    rec_len=[]
    with conn.cursor() as cur:
        for i in range(len(komat_id)):
            sql='select count(time) from %s'%komat_id[i]
            cur.execute(sql)
            ret=cur.fetchall()
            rec_len.append(ret[0])
    return rec_len

if __name__=="__main__":
    host='localhost'
    user='root'
    password='password'
    db='408data'
    table_1='A01_CCMT060204_EMF_01'
    table_2='a01'
    experimental_group_1='A01_CCMT060204-EMF_01'
    conditionPlot(host,user,password,db,table_1,table_2)