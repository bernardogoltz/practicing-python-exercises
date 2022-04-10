# -*- coding: utf-8 -*-
"""
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
"""

name = str(input("Insira seu nome: "))

for i in enumerate(name):
    print(i[1])
    
    # python é elegante :) 