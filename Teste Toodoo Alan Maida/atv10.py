# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:02:08 2021

@author: aland
"""


import sys
import numpy as np


x=int(input("Informe um número para ver seu fatorial:"))
y=x

for i in range(1,x):
    y=y*(x-i)

print("O fatorial de",x,"é igual:",y)








