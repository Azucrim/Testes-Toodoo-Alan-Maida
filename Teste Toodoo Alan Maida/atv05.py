# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 19:29:51 2021

@author: aland
"""

import sys
import numpy as np




A=int(input('A: '))
B=int(input('B: '))
print("")


if A>B:
    if (A%B)==0:
        print("Os dois números são múltiplos")
    else:
        print("Os dois números não são múltiplos")

else:
    if (B%A)==0:
        print("Os dois números são múltiplos")    
    else:
        print("Os dois números não são múltiplos") 

print("")
