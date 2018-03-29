# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 19:40:37 2018

@author: hasee
"""

from __future__ import print_function

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import numpy as np
import pandas as pd
from pandas.tools.plotting import scatter_matrix

from sqlalchemy import create_engine

def kCondition(table):
    '''
    Import Data
    '''
    
    engine=create_engine("mysql+pymysql://root:password@localhost/408data")
    sql='select spindle_torque,spindle_actual_speed,x_p_diff,y_p_diff,z_p_diff from %s'%table
    X=pd.read_sql(sql,engine).astype(float)
    
    #range_n_clusters：A range of clustering numbers
    range_n_clusters = list(range(2,1001))
    
    '''
    Calculate the silhouette score, plot, and scatter matrix
    '''
    
    for n_clusters in range_n_clusters:
        fig1=plt.figure()
        fig1.set_size_inches(10, 7)
        ax1 = fig1.add_subplot(111)
        ax1.set_xlim([-1, 1])
        ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])
        
        clusterer = KMeans(n_clusters=n_clusters, random_state=10)
        cluster_labels = clusterer.fit_predict(X)
        
        silhouette_avg = silhouette_score(X, cluster_labels,block_size=1024,n_jobs=2)
        
        # average silhouette_score output to .txt
        with open('D:\\img\\out.txt','a') as f:
            print("For n_clusters =", n_clusters,
                  "The average silhouette_score is :", silhouette_avg, file=f)
            
        sample_silhouette_values = silhouette_samples(X, cluster_labels,block_size=1024,n_jobs=2)
        
        #plot ax1
        y_lower = 10
        for i in range(n_clusters):
            ith_cluster_silhouette_values = \
            sample_silhouette_values[cluster_labels == i]
            
            ith_cluster_silhouette_values.sort()
            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i
            
            color = cm.spectral(float(i) / n_clusters)
            ax1.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)
#            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
            y_lower = y_upper + 10
            
        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")
        ax1.set_yticks([])
        ax1.set_xticks([-1,-0.8,-0.6,-0.4,-0.2, 0, 0.2, 0.4, 0.6, 0.8, 1])
        plt.savefig('D:\\img\\'+str(n_clusters)+'_1.png',dpi=300)
        
        #plot ax2
        fig2=plt.figure()
        fig2.set_size_inches(30, 30)
        ax2 = fig1.add_subplot(111)
        ax2=scatter_matrix(X,figsize=[28,24],c='g',alpha=0.2,diagonal='kde',s=30,marker='.')
        
#        centers = clusterer.cluster_centers_
#        ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
#                c="white", alpha=1, s=200, edgecolor='k')
        
        [s.xaxis.label.set_rotation(45) for s in ax2.reshape(-1)]
        [s.yaxis.label.set_rotation(0) for s in ax2.reshape(-1)]
        [s.get_yaxis().set_label_coords(-0.4,0.5) for s in ax2.reshape(-1)]
        [s.set_xticks(()) for s in ax2.reshape(-1)]
        [s.set_yticks(()) for s in ax2.reshape(-1)]
        [s.xaxis.get_label().set_fontsize(22) for s in ax2.reshape(-1)]
        [s.yaxis.get_label().set_fontsize(22) for s in ax2.reshape(-1)]
        plt.savefig('D:\\img\\'+str(n_clusters)+'_2.png',dpi=300)
#        print(X)
if __name__=="__main__":
    table='A01_CCMT060204_EMF_01_condition'
    kCondition(table)