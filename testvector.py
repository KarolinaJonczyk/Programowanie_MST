#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:55:58 2022

@author: karolinajonczyk
"""

import basevector
import numpy as np

vector1=basevector.BaseVector()

vector2=basevector.BaseVector()

print("check is vector length 5: ", basevector.BaseVector(5))

#expected: vector length 3
print("check default vector: ", basevector.BaseVector())

print("first vector is: ", vector1.random())
print("second vector is: ", vector2.random())
print("check overwrite: ", vector1.overwrite(np.array([2,1,-1])))
print("test __add__ :", vector1.__add__(vector2))
print("test __sub__ :", vector2.__sub__(vector2))
print("test __mul__ :", vector1.__mul__(7))
print("test size:", vector1.size)
print("test length:", vector1.length())
print("test sum:", vector1.sum())
print("test __str__:", vector1.__str__())
print("test __repr__:", vector1.__repr__())
print("test scalar_product:", vector1.scalar_product(vector2))
print("test __getitem__:", vector1.__getitem__(vector1[2])) 
print("test __contains__:", vector1.__contains__(vector1[0]))
