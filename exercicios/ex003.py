# -*- coding: utf-8 -*-
"""
Faça um Programa que peça dois números e imprima a soma.

"""

a = float(input("Insira um numero: "))
b = float(input("Insira um numero: "))

def soma(a,b):
    return a + b 

print("{} + {} = {}".format(a,b,soma(a,b)))
