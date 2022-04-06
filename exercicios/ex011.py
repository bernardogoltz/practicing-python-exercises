# -*- coding: utf-8 -*-
"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    
o produto do dobro do primeiro com metade do segundo .

a soma do triplo do primeiro com o terceiro.

o terceiro elevado ao cubo

"""

i = int(input("inteiro 1: "))
j = int(input("inteiro 2: "))
n = float(input("real: "))


def produto(i,j):
    return (i*2) + (j/2)

def soma(i,n):
    a = float(i)
    return (a*3) + n
        
def cubo(n):
    return pow(n,3)

print(produto(i,j))
print(soma(i,n))
print(cubo(n))