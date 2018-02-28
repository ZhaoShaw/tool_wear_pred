# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:45:09 2018

@author: hasee
"""

from functools import wraps

def decorator(arg1,arg2):
    def inner_func(func):
      @wraps(func)
      def wrapper(*args,**kw):
          print('Arguements passed to decorator %s and %s'%(arg1,arg2))
          func(*args,**kw)
      return wrapper
    return inner_func

@decorator('arg1','arg2')
def print_args(*args):
    for arg in args:
        print(arg)

print(print_args(1,2,3))#None 来自哪里？