# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:07:16 2018

@author: hasee
"""

import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

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
def kMeans(dataSet,k,maxIter=2):
    '''
    K-Means
    Args:
        dataSet:数据集
        k:聚类数
    Returns:
        centroids:聚类中心
        clusterAssment:点分配结果
    '''
    # 随机初始化聚类中心
    centroids=randCent(dataSet,k)
    m,n=np.shape(dataSet)# m是样本点数
     # 点分配结果： 第一列指明样本所在的簇，第二列指明该样本到聚类中心的距离
    clusterAssment=np.mat(np.zeros((m,2)))
    clusterChanged=True
    iterCount=0
    while clusterChanged and iterCount < maxIter:#聚类中心不再改变，或循环达到maxIter，给出结果
        iterCount+=1
        clusterChanged=False
        # 分配样本到簇
        for i in range(m):
            minIndex=0
            minDist=np.inf
            for j in range(k):
                dist=disEclud(dataSet.iloc[i:i+1,:],centroids[j,:])
                if(dist.item()<minDist):
                    minIndex=j
                    minDist=dist.item()
            if (clusterAssment[i,0] != minIndex):
                clusterChanged=True
            clusterAssment[i,:]=minIndex,minDist**2
        # 刷新聚类中心: 移动聚类中心到所在簇的均值位置
        for cent in range(k):
            ptsInCluster=dataSet.iloc[np.nonzero(clusterAssment[:,0]==cent)[0]]
            if ptsInCluster.shape[0]>0:
                centroids[cent,:]=np.mean(ptsInCluster,axis=0)
    return centroids,clusterAssment
                
def disEclud(vecA,vecB):
    '''
    计算两向量的欧氏距离
    '''
    return np.sqrt(np.sum(np.power(vecA-vecB,2)))

def plotRes(dataset,centroids,clusterAssment,k,color):
    '''
    画图(针对数据集，这里仅限2维图)
    Args:
        centroids:聚类中心
        clusterAssment:点分配结果
        k:聚类数
        color:颜色
    Return:
        Plot
    '''
    plt.figure(figsize=(100,60))
    for cent in range(k):
        x=dataset.iloc[np.nonzero(clusterAssment[:,0]==cent)[0]]
        plt.plot(x,color=color[cent],marker='.')
        plt.plot(centroids[cent,:],color=color[cent],marker='o',markersize=20.0)
    plt.show()
if __name__=="__main__":
    engine=create_engine("mysql+pymysql://root:password@localhost/408data")
    dataset=pd.read_sql('a01_ccmt060204_emf_01_condition',engine,columns=['spindle_torque'])
#    index_col=['time']
    k=2 #聚类中心
    color=['r','b']
    centroids,clusterAssment=kMeans(dataset,k)
    plotRes(dataset,centroids,clusterAssment,k,color)