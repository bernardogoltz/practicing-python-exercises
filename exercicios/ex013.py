# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:04:03 2022

@author: bernardogoltz
"""

def factorial(x):
    
    if x == 1:
        return 1
    
    else:
        return(x*factorial(x-1))
    
num = int(input("insira um numero: "))
print("o fatorial de {} é {}".format(num,factorial(num)))