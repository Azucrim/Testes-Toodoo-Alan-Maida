# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 22:11:02 2021

@author: aland
"""


import sys
import numpy as np


pn=str(input("Informe uma palavra:"))
pi=""

for i in range(len(pn)):
    pi+=pn[(len(pn)-1)-i]
    
    
if pn==pi:
    print("A palavra",pn,"é um palíndromo")
else:
    print("A palavra",pn,"não é um palíndromo")
    











