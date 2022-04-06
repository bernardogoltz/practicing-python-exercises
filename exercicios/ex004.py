# -*- coding: utf-8 -*-
"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""
import numpy as np

notas = np.zeros(4)
amount = 0 

for i in range(len(notas)):
    
    notas[i] = float(input("nota{}: ".format(i)))

    amount = amount + notas[i] 
    media = amount/len(notas)
    
print(media)
    
     
#print("Média: {} ".format(notas.mean()))


