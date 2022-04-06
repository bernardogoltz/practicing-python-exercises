# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:19:02 2022

@author: bernardogoltz
"""

cat_o = float(input("Cateto oposto: "))
cat_a = float(input("Cateto adjacente: "))

import numpy as np

hipotenusa = np.sqrt((pow(cat_o,2)+pow(cat_a,2)))

print("hipotenusa = {}".format(hipotenusa))
