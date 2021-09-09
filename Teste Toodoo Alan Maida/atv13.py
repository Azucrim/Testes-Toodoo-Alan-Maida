# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:32:14 2021

@author: aland
"""

import sys
import numpy as np


i=int(input("Quantidade de Linhas:"))
z=int(input("Quantidade de Colunas:"))

m=[]


for x in range(i):
    m.append([])
    for y in range(z):        
        m[x].append((y+1)*(x+1))

for x in range(i):
    for y in range(z):
        print("[",m[x][y],"]", end='')
    print()
        



