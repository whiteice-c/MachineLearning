# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:09:37 2019

@author: baibing
"""

import tensorflow as tf

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],[2]])
predict = tf.matmul(matrix1,matrix2)

#method1 
#sess = tf.Session()
#result = sess.run(predict)
#print(result)
#sess.close()

#method2
with tf.Session() as sess:
    result = sess.run(predict)
    print(result)