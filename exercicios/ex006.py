# -*- coding: utf-8 -*-
"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

"""

import numpy as np

pi = round(np.pi,5)

def area(raio):
    return pi * pow(raio,2)

raio = float(input("Raio (m) = "))

print("Um círculo com {}m de raio produz uma área de {}m²".format(raio, area(raio)))


