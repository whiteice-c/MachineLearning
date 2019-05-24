# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 18:13:34 2019

@author: baibing
"""

import tensorflow as tf

num = tf.Variable(0,name = 'counter')
one = tf.constant(1)

#print(num.name)

new_value = tf.add(num,one)
update = tf.assign(num,new_value)

init = tf.initialize_all_variables() #nust do if define variable

with tf.Session() as sess:
    sess.run(init)#must have,real init
    for _ in range(3):
        sess.run(update)
        print(sess.run(num))