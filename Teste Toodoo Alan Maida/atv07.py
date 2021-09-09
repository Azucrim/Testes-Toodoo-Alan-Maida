# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 20:21:32 2021

@author: aland
"""

import sys
import numpy as np


intervalo=int(input('Intervalo: '))

vs=[]

vet=np.random.randint(1,100,intervalo)
print('Vetor gerado',vet)

for i in range(intervalo):
    if (vet[i]%2)==0:
        vs.append(vet[i])
        
print('Lista de pares',vs)
