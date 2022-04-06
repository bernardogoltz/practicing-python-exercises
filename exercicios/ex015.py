# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:16:12 2022

@author: bernardogoltz
@title: ler um float e mostrar a parte inteira

"""

n_float = float(input("Float: "))

n_int = int(round(n_float))

print("Parte inteira = {}".format(n_int))
