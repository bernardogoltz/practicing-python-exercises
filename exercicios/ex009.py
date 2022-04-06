# -*- coding: utf-8 -*-
"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

C = 5 * ((F-32) / 9).
"""

temp_f = float(input("temperatura em F: "))

def f2c(temp_f):
    return 5 * ((temp_f-32)/9)

temp_c = f2c(temp_f)

print("{}F = {}C".format(temp_f , temp_c))