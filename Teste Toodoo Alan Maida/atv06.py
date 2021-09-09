# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 19:45:56 2021

@author: aland
"""

import sys
import numpy as np
#import time
import datetime
#from datetime import datetime

import datetime

ti = input('Entre a hora de início do jogo no formato hh:mm:ss:')
h1, m1, s1 = map(int, ti.split(':'))
t1 = datetime.time(h1, m1, s1)

tf = input('Entre a hora de término do jogo no formato hh:mm:ss:')
h2, m2, s2 = map(int, tf.split(':'))
t2 = datetime.time(h2, m2, s2)

print('Hora de início do jogo:',t1)
print('Hora de término do jogo:',t2)

tdif = datetime.time(h2 - h1, m2 - m1, s2 - s1)
print('Duração do Jogo:',tdif)