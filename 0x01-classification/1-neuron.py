#!/usr/bin/env python3
import numpy as np
class Neuron:
    def __init__(self, nx):
        '''INTEGER CONDITION'''
        if type(nx) != int:
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')
        else:
            self.__W = np.random.normal(size=(1, nx))
            self.__b = 0
            self.__A = 0
             
    @property
    def W(self):
        """Returns: private instance weight"""
        return self.__W

    @property
    def b(self):
        """Returns: private instance bias"""
        return self.__b

    @property
    def A(self):
        """Returns: private instance output"""
        return self.__A
