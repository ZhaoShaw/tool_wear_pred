# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:59:23 2018

@author: hasee
"""
#error code:使用tf.get_variable()创建变量，且没有设置共享变量，重名时会报错
import tensorflow as tf 

with tf.name_scope('name_scope_1'):
    var1=tf.get_variable(name='var1',shape=[1],dtype=tf.float32)
    var2=tf.get_variable(name='var1',shape=[1],dtype=tf.float32)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(var1.name,sess.run(var1))
    print(var2.name,sess.run(var2))