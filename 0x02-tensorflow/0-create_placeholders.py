#!/usr/bin/env python3
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def create_placeholders(nx, classes):
    '''x is the placeholder for the input data to the neural network'''
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    
    '''y is the placeholder for the one-hot labels for the input data'''
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')
    return x,y
