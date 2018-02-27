# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 12:05:27 2018

@author: hasee
"""
#共享变量，需要使用tf.variable_scope()
import tensorflow as tf 

with tf.variable_scope('variable_scope_y') as scope:
    var1 = tf.get_variable(name='var1',shape=[1],dtype=tf.float32)
    scope.reuse_variables() #共享变量
    var1_reuse = tf.get_variable(name='var1')
    var2 = tf.Variable(name='var2',initial_value=[2.],dtype=tf.float32)
    var2_reuse = tf.Variable(name='var2',initial_value=[2.],dtype=tf.float32)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(var1.name,sess.run(var1))
    print(var1_reuse.name,sess.run(var1_reuse))
    print(var2.name,sess.run(var2))
    print(var2_reuse.name,sess.run(var2_reuse))
