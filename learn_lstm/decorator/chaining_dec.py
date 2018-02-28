# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:22:17 2018

@author: hasee
"""

def makebold(f):
    return lambda:'<b>'+f()+'</b>'
def makeitalic(f):
    return lambda:'<i>'+f()+'</i>'

@makebold
@makeitalic
def say():
    return 'Hellow'

print(say())