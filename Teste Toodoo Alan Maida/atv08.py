# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:34:25 2021

@author: aland
"""

import sys
import numpy as np

x=int(input("Informe um número:"))

if x>3:
    if ((x%2)==0) or ((x%3)==0):
        print(x,"não é primo")
    else:
        print(x,"é primo")

else:
    if x<=1:
        print(x,"não é primo")
    else:
       print(x,"é primo") 

        




