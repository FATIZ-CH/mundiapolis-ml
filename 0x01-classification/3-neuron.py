#!/usr/bin/env python3
import numpy as np
class Neuron:

    def __init__(self, nx):
        """
        constructeur de la classe
        la variable nx: est le nombre d'entités d'entrée du neurone
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.nx = nx
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    def forward_prop(self, X):
        """
        calcule de la propagation avant du neurone
        """
        preactivation = np.matmul(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-preactivation))
        return self.__A

    def cost(self, Y, A):
        """
         le calcule du coût du modèle à l'aide de la régression logistique
        retourne: le coût
        """
        cost = Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)
        cost = np.sum(cost)
        cost = - cost / A.shape[1]
        return cost

    @property
    def W(self):
        """
        fonction getter pour W
        elle retourne: vecteur de poids du neurone
        """
        return self.__W

    @property
    def b(self):
        """
        fonction getter pour b
        elle retourne: biais pour le neurone
        """
        return self.__b

    @property
    def A(self):
        """
        fonction getter pour A
        elle retourne: sortie activée du neurone
        """
        return self.__A
