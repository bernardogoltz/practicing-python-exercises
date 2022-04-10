# -*- coding: utf-8 -*-
"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO

"""

name = str(input("Insira o seu nome: "))
for i in range(len(name)+1):
    print(name[:i])
    
    