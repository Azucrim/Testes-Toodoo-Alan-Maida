# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:32:20 2021

@author: aland
"""

import sys
import numpy as np


n=3
l=["A","B","C"]

v=[]

for i in range(n):
    v.append(float(input(l[i]+'= ')))
    

menor=min(v)   


print("V=",v,", e seu menor volor é:",menor)


