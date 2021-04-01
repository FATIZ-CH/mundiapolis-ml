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
            self.W = np.random.normal(size=(1, nx))
            self.b = 0
            self.A = 0
             
    def forward_prop(self, X):
        """Returns: biais pour le neurone"""
        x = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-x))
        return self.__A
           
    @property
    def W(self):
        """Returns: Value of __W"""
        return self.__W

    @property
    def b(self):
        """Returns: private instance bias"""
        return self.__b

    @property
    def A(self):
        """Returns: private instance output"""
        return self.__A

    
