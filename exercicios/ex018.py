# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:28:41 2022

@author: bernardogoltz
@title: sorteio

"""
import random

n = 4
names_list = []

for i in range(n):
    
    name = str(input("name{}: ".format(i+1)))
    names_list.append(name)
    
def sortition(list_):
    return random.choice(list_)

print("the lucky one is: {} ".format(sortition(names_list)))
    
   
    
    