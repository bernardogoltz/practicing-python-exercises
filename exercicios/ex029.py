# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:10:16 2022

@author: bernardogoltz
"""

def analisaSinal(argumento):
    
    if argumento > 0:
        return 'p'
    
    elif argumento == 0:
        return 'z'
    
    elif argumento < 0:
        return 'n'
    
    else:
        return "Argumento inválido"
    
for i in range(-2,2):
    
    print(analisaSinal(i))
    
    """
    output : 
        
    - n
    - n
    - z
    - p
    
    """