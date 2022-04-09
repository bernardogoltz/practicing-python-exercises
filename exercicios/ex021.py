# -*- coding: utf-8 -*-
"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

"""

numeros = []

for i in range(10):
    
    numero = int(input("números: {} -> ".format(i+1)))
    numeros.append(numero)
    
numeros_reverso = list(reversed(numeros))
print(numeros_reverso)