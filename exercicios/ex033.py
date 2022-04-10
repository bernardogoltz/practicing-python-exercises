# -*- coding: utf-8 -*-
"""
Nome na vertical em escada invertida.
Altere o programa anterior de modo que a escada seja invertida.
"""

name = "bernardo"

#str(input("Insira o seu nome: "))

for i in range(len(name)):
    if i == 0:
        print(name)
    
    else:    
        print(name[:-i])
        
# solução nada elegante para um bug que eu não compreendi, se você está lendo isso saiba que: 1 - sua existência nesse momento fazendo o que está fazendo é improvável, então considere-se único e 2 - provavelmente você vive em um futuro em que eu já sei percorrer strings em python... de qualquer forma, obrigado por estar aqui... 
    