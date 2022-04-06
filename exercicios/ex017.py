# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:24:01 2022

@author: bernardogoltzz
"""
import numpy as np

alpha = float(input("Input the angle value in degrees: "))
alpha = np.radians(alpha)

sin = round(np.sin(alpha),2)
cos = round(np.cos(alpha),2)
tan = round(np.tan(alpha),2)

print("sin = {}".format(sin))
print("cos = {}".format(cos))
print("tan = {}".format(tan))