# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:50:54 2018

@author: hasee
"""
class ClassDecorator(object):
    
    def __init__(self,arg1,arg2):
        print ('Arguements passed to decorator %s and %s' % (arg1, arg2))
        self.arg1=arg1
        self.arg2=arg2
    
    def __call__(self,foo,*args,**kw):
        def inner_func(*args,**kw):
            print ('Args passed inside decorated function .%s and %s' % (self.arg1, self.arg2))
            return  foo(*args,**kw)
        return inner_func
            
        
@ClassDecorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1,2,3)