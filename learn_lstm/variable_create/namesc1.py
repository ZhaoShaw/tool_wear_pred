# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:56:27 2018

@author: hasee
"""
#在 tf.name_scope下时，tf.get_variable()创建的变量名不受 name_scope 的影响，而且在未指定共享变量时，如果重名会报错，tf.Variable()会自动检测有没有变量重名，如果有则会自行处理。
import tensorflow as tf 

with tf.name_scope('name_scope_x'):
    var1 = tf.get_variable(name='var1',shape=[1],dtype=tf.float32)
    var3 = tf.Variable(name='var2',initial_value=[2],dtype=tf.float32)
    var4 = tf.Variable(name='var2',initial_value=[2],dtype=tf.float32)
    
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(var1.name,sess.run(var1))
    print(var3.name,sess.run(var3))
    print(var4.name,sess.run(var4))