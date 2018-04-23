# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 21:15:13 2018

@author: hasee
"""

import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import PolynomialFeatures,Imputer

from sqlalchemy import create_engine
from sklearn.decomposition import PCA

def toolScal(table):
    engine=create_engine("mysql+pymysql://root:****@localhost/****")
    sql='select spindle_torque,spindle_actual_speed,x_p_diff,y_p_diff,z_p_diff from %s'%table
    X=pd.read_sql(sql,engine).astype(float) 
    
    imp=Imputer(missing_values='NaN', strategy='mean', axis=0).fit(X)
    X_imp=imp.transform(X)
    
#    std_scale=preprocessing.StandardScaler().fit(X)
#    X_std=std_scale.transform(X)
    
    poly = PolynomialFeatures(2,include_bias=False)
    X_ploy=poly.fit_transform(X_imp)
    columns=poly.get_feature_names()
    
    rob_scale=preprocessing.RobustScaler().fit(X_ploy)
    X_rob=rob_scale.transform(X_ploy)
    
    normalizer = preprocessing.Normalizer().fit(X_rob)
    X_nor=normalizer.transform(X_rob)
	
#    pca = PCA(n_components=0.99999)
#    pca.fit(X_rob)
#    print(pca.components_)
#    print(pca.n_components_)
#    print(pca.explained_variance_ratio_)
#    print(pca.explained_variance_)
    
    X_rob_df=pd.DataFrame(X_nor,columns=columns)
    X_rob_df.to_sql(name='scal'.lower(),con=engine,if_exists='replace')
    
    np.savetxt(r'd:\scal.txt', X_nor, fmt='%.10e',delimiter=',',newline='\r\n')
    
#    print(X)
if __name__=="__main__":
    table='A01_CCMT060204_EMF_01_condition'
    toolScal(table)