#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:53:14 2022
Last update: Tue Dec 12 11:49:14 2023
@author: karolinajonczyk
"""

import numpy as np


class BaseVector():
    def __init__(self, size=None):
        """Constructor"""
        self.size = size if size is not None else 3
        self.vector=np.ones(self.size,dtype=np.float64)

    def random(self):
        """Method for randomly generating vector elements"""
        rand=np.random.randint(0,100,size=self.size)
        self.vector *= rand
        print(f'Wylosowano wektor: {self.vector}')
        return self.vector

    def overwrite(self, vector):
        """Method for loading vector elements from a list provided as an argument"""
        self.vector=vector
        print(f'Zapisano wektor: {self.vector}')
        return self.vector

    def __add__(self, other):
        """Operator adding two vectors"""
        return np.add(self.vector , other.vector)
    
    def __sub__(self, other):
        """Operator subtracting two vectors"""
        return np.subtract(self.vector , other.vector)

    def __mul__(self, scalar):
        """Vector multiplication by scalar"""
        return  self.vector*scalar

    def size(self):
        """Method checking the size of a vector"""
        return len(self.vector)

    def length(self):
        """Method calculating the length of a vector"""
        return np.linalg.norm(self.vector)

    def sum(self):
        """Method calculating the sum of vector elements"""
        return np.sum(self.vector)

    def __str__(self):
        """Text representation of a vector - generating a string"""
        return str(self.vector)

    def __repr__(self):
        """Text representation of a vector"""
        return print(self.vector)

    def scalar_product(self, other):
        """Method calculating the dot product of two vectors"""
        return np.dot(self.vector,other.vector)

    def __getitem__(self, a):
        """Operator [] allowing access to specific elements of a vector"""
        return self.vector[a]

    def __contains__(self, a):
        """Operator checking the inclusion of an element in a vector"""
        if a in self.vector:
            return True
        else:
            return False
