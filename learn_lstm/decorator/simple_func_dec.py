# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:49:26 2018

@author: hasee
"""
import time 
def timeset(func):
    def wrapper(*args,**kw):
        start_time=time.time()
        end_time=time.time()
        result=func(*args,**kw)
        print('Method Name - {0},Args - {1},Kw - {2},Execution - {3}'.format(func.__name__,
              args,kw,end_time-start_time))
#        result=func(*args,**kw)
        return result
    return wrapper
@timeset
def foobar(*args,**kw):
    time.sleep(0.5)
    print('inside foobar')
    print(args,kw)

foobar(['hellow,world'],foo=2,bar=5)
