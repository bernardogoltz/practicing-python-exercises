# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:08:23 2022

@author: bernardogoltz
@title: sequência de fibonacci

"""

n = int(input("n de termos? "))

a = 0
b = 1
x = 0

for i in range(n):

    print("{} ".format(x), end = "")
    
    x = a + b
    
    b = a 
    a = x 
    
    
    
    
    



