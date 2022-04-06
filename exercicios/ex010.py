# -*- coding: utf-8 -*-

"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

temp_c = float(input("Temperatura em C: "))


def c2f(temperatura_em_celsius):
    return (1.8*temperatura_em_celsius) + 32
    
temp_f = c2f(temp_c)
print("{}C = {}F".format(temp_c , temp_f))