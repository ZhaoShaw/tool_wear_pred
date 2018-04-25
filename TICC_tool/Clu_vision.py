# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:32:14 2018

@author: hasee
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sqlalchemy import create_engine

def Clu_vision(table,K):
    engine=create_engine("mysql+pymysql://root:******@localhost/******")
    sql='select **** from %s'%table
    X=pd.read_sql(sql,engine).astype(float)
#    color = cm.spectral(float(i) / n_clusters)
    results=pd.read_csv(r'd:\Workplace\***.txt',
                        header=None,names=['clu']).astype(int)
    mis_dt=[]
    for i in range(X.size-results.size):
        mis_dt.insert(0,{'clu':results.iat[0,0]}) 
        
    results=pd.concat([pd.DataFrame(mis_dt),results],ignore_index=True)
    
    X_concat=pd.concat([X,results],axis=1)
    
    fig, ax = plt.subplots(figsize=(30,30))
    
    colors=[]
    for i in range(K):
        colors.append(cm.spectral(float(i)/K))
        
    blo=[-1]
    for i in range(X_concat.shape[0]-1):
        if X_concat.iat[i,1]==X_concat.iat[i+1,1]:
            continue
        else:
            blo.append(i)
    blo.append(X_concat.shape[0]-1)
    np.savetxt(r'd:\Workplace\clu.txt',blo,fmt='%d',delimiter=',',newline='\r\n')
    
    for i in range(len(blo)-1):
        temp=list(range(blo[i]+1,blo[i+1]+1))
        ax.plot(temp,X_concat.loc[temp[0]:temp[-1],['*****']],
                color=colors[X_concat.iloc[blo[i+1],1]])
    
    ax.set(xlabel='time', ylabel='****')
    ax.set_yticks([])
    plt.savefig('D:\\Workplace\\clu.png',dpi=300)
    plt.show()
#    print(X)
if __name__=="__main__":
    table='******'.lower()
    K=20
    Clu_vision(table,K)
