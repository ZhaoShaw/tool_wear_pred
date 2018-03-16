# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:25:24 2018

@author: hasee
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataSet=pd.DataFrame(np.random.randint(low=0, high=10, size=(1000, 2)),columns=['a', 'b'])
a=np.array([[0,0],[1,2],[1,2]])
b=dataSet.iloc[np.nonzero(a[:,0]==1)[0]]
plt.figure(figsize=(20,10))
plt.plot(b.iloc[:,0],b.iloc[:,1],'r.')
plt.plot(a[:,0],a[:,1],'b.')
#plt.plot(dataSet.iloc[:,0],dataSet.iloc[:,1],'y.')
plt.show()