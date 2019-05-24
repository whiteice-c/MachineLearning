# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 19:02:26 2019

@author: baibing
"""

import tensorflow as tf

input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1,input2)

#当变量用placeholder设置时，想调用通过这些变量运算获取的其他变量时，只需在获取
#时再赋予这些变量的值，形式为字典，如下
with tf.Session() as sess:
    print(sess.run(output,feed_dict = {input1:[7.0],input2:[2.0]}))