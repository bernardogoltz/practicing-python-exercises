# -*- coding: utf-8 -*-
"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""

def soma(a,b,c):
    return a+b+c

x = input("primeiro argumento: ")
y = input("segundo argumento: ")
z = input("terceiro argumento: ")

x,y,z = float(x) , float(y) , float(z)

print("A soma dos três argumentos é: {}".format(soma(x,y,z)))