# -*- coding: utf-8 -*-
"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
import statistics 

notas = []
n = 4

nota_cumulativa = 0 

for i in range(4):
    
    nota = float(input("Nota {}: ".format(i+1)))
    notas.append(nota)
    
media = statistics.mean(notas)

# poderia ter usado uma variavel cumulativa somar as notas e dividir pelo len() do respectivo vetor, no entanto, acredito que utilizando a statistics.mean() o código fica mais elegante e legível. 

print("A média é {}".format(media))
    
    
   

