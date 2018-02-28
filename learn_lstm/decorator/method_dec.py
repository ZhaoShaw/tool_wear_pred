# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:55:26 2018

@author: hasee
"""
from functools import wraps
def method_dec(method):
    @wraps(method)
    def inner(city_instance):
        if city_instance.name == 'Xi\'an':
            print('It is a beautiful city')
        else:
            method(city_instance)
    return inner

class City(object):
    def __init__(self,name):
        self.name=name
    @method_dec
    def print_test(self):
        print(self.name)
p1=City('Xi\'an')

p1.print_test()

p2=City('TW')

p2.print_test()
