# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:44:02 2022

@author: bernardogoltz

Para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

"""

n = int(input("insira  n (n-ésima linha) : "))

def nlinhas(n_linhas):
    
    if n > 0:
        for i in range(n):
            n_str = str(n)*(i+1)
            print(n_str)
    
    elif n == 0:
        print(n)
    
    elif n < 0:
        
        aux = abs(n)
        for i in range(abs(n)):
            print("{}".format(str(abs(n-4))*aux))
            aux = aux - 1
            
nlinhas(n)
            
                
     
            


        
