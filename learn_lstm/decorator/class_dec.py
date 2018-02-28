# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 16:50:51 2018

@author: hasee
"""

class class_dec(object):
    def __init__(self,func):
        self._func=func
    def __call__(self,*args,**kw):
        print('func begin')
        self._func(*args,**kw)
        print('func end')

@class_dec
def f():
    print('class')

f()