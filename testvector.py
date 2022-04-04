#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:55:58 2022

@author: karolinajonczyk
"""

import basevector
import numpy as np

#ustalmy ułatwienie do testowania: p - pierwszy wektor, d - drugi wektor
p=basevector.BaseVector()

d=basevector.BaseVector()

#sprawdzamy wektor o rozmiarze 5
print("sprawdzamy konkretny: ", basevector.BaseVector(5))

#sprawdzamy czy wyrzuci nam wektor o rozmiarze 3, bo tak zakladamy domyślnie
print("sprawdzamy domyślny: ", basevector.BaseVector())


print("wektor pierwszy ma postać: ", p.random())
print("wektor drugi ma postać: ", d.random())
print("sprawdzamy overwrite: ", p.overwrite(np.array([2,1,-1])))
print("test __add__ :", p.__add__(d))
print("test __sub__ :", p.__sub__(d))
print("test __mul__ :", p.__mul__(7))
print("test size:", p.size)
print("test length:", p.length())
print("test sum:", p.sum())
print("test __str__:", p.__str__())
print("test __repr__:", p.__repr__())
print("test scalar_product:", p.scalar_product(d))
print("test __getitem__:", p.__getitem__(p[2])) 
print("test __contains__:", p.__contains__(p[0]))
