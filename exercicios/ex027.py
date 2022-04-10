# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:44:02 2022

@author: bernardogoltz

1
1   2
1   2   3

Para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

"""

n = int(input("insira  n (n-ésima linha) : "))

def nlinhas(n):

    linha = ""
    
    for i in range(1,n+2):
        
        aux = str(i)
        print(linha)
        
        linha = linha + aux + " "
        
                
nlinhas(n)   