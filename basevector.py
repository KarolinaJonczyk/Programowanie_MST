#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 21:53:14 2022

@author: karolinajonczyk
"""

import numpy as np


class BaseVector():
    def __init__(self, size=None):
        """Konstruktor"""
        self.size = size if size is not None else 3
        self.vector=np.ones(self.size,dtype=np.float64)

    def random(self):
        """Metoda do losowej generacji elementów wektora """
        rand=np.random.randint(0,100,size=self.size)
        self.vector *= rand
        print(f'Wylosowano wektor: {self.vector}')
        return self.vector

    def overwrite(self, vector):
        """Metoda do wczytywania elementów wektora z listy podanej jako argument"""
        self.vector=vector
        print(f'Zapisano wektor: {self.vector}')
        return self.vector

    def __add__(self, other):
        """Operator dodawania dwóch wektorów"""
        return np.add(self.vector , other.vector)
    
    def __sub__(self, other):
        """Operator odejmowania dwóch wektorów"""
        return np.subtract(self.vector , other.vector)

    def __mul__(self, scalar):
        """Mnożenie wektora przez skalar"""
        return  self.vector*scalar

    def size(self):
        """Metoda sprawdzająca rozmiar"""
        return len(self.vector)

    def length(self):
        """Metoda wyliczającą długość wektora"""
        return np.linalg.norm(self.vector)

    def sum(self):
        """Metoda wyliczającą sumę elementów wektora"""
        return np.sum(self.vector)

    def __str__(self):
        """Reprezentacja tekstowa wektora - generujemy stringa"""
        return str(self.vector)

    def __repr__(self):
        """Reprezentacja tekstowa wektora - możemy printować"""
        return print(self.vector)

    def scalar_product(self, other):
        """Metoda wyliczającą iloczyn skalarny dwóch wektorów"""
        return np.dot(self.vector,other.vector)

    def __getitem__(self, a):
        """Operator [] pozwalający na dostęp do konkretnych elementów wektora"""
        return self.vector[a]

    def __contains__(self, a):
        """Operator in sprawdzający przynależność elementu do wektora."""
        if a in self.vector:
            return True
        else:
            return False