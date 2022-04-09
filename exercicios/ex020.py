# -*- coding: utf-8 -*-
"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
"""

n = 5 
numeros = []

for i in range(n):
    numero = float(input("número{} = ".format(i+1)))
    numeros.append(numero)

print("="*50)
print("   Os numeros escolhidos foram: {}".format(numeros))
print("="*50)