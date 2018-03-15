# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:07:16 2018

@author: hasee
"""

import numpy as np
import pandas as pd
import pymysql
from sqlalchemy import create_engine

def randCent(dataSet,k):
    '''
    随机生成k个聚类中心
    
    Args:
        dataSet:数据集
        k:簇数目
    Returns:
        centroids:聚类中心矩阵
    '''
    _,n=dataSet.shape
    centroids=np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ=np.min(dataSet.iloc[:,j:j+1])
        maxJ=np.max(dataSet.iloc[:,j:j+1])
        rangeJ=float(maxJ-minJ)
        centroids[:,j]=np.random.rand(k,1)*rangeJ+minJ[0]
    return centroids
def kMeans(dataSet,k,maxIter=5):
    '''
    K-Means
    Args:
        dataSet:数据集
        k:聚类数
    Returns:
        centroids:聚类中心
        clusterAssment:点分配结果
    '''
    centroids=randCent(dataSet,k)
    m,n=np.shape(dataSet)
    clusterAssment=np.mat(np.zeros(m,2))
    clusterChangd=True
    iterCount=0
    while clusterChanged and iterCount < maxIter:
        iterCount+=1
        clusterChanged=False
        for i in range(m):
            minIndex=0
            minDist=np.inf
            for j in range(k):
                dist=disEclud(dataSet[i,:],centroids[j,:])
                if(dist<minDist):
                    minIndex=j
                    minDist=dist
            if (clusterAssment[i,0] != minIndex):
                clusterChanged=True
            clusterAssment[i,:]=minIndex,minDist**2
        for cent in range(k):
            ptsInCluster=dataSet[np.nonzero(clusterAssment[:,0].A==cent)[0]]
            if ptsInCluster.shape[0]>0:
                centroids[cent,:]=np.mean(ptsInCluster,axis=0)
    return centroids,clusterAssment
                
def disEclud(vecA,vecB):
    '''
    计算两向量的欧氏距离
    '''
    return np.sqrt(np.sum(np.power(vecA-vecB,2)))
    
if __name__=="__main__":
    engine=create_engine("mysql+pymysql://root:password@localhost/408data")
    dataset=pd.read_sql('a01_ccmt060204_emf_01_condition',engine,index_col=['time'],columns=['spindle_torque'])
    centroids,clusterAssment=kMeans(dataset,100)