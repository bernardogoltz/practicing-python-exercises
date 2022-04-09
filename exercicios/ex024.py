# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:16:27 2022

Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor

@author: bernardogoltz
"""


vetor = []
n = 2

somatorio = 0 

for i in range(n):

    elemento = int(input("num{}: ".format(i+1)))
    vetor.append(elemento)
    
    somatorio = somatorio + vetor[i]
    
resultado = pow(somatorio,2)
print("{}² = {}".format(somatorio, resultado))