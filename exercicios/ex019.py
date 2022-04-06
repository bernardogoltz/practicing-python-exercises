# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:44:05 2022

@author: bernardogoltz
@title: sort order

"""

from random import shuffle

n = 4
names_list = []

for i in range(n):
    
    name = str(input("name{}: ".format(i+1)))
    names_list.append(name)

shuffle(names_list)

print("A ordem de apresentação será: ")
print(names_list)