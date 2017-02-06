# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:03:07 2017

@author: Drew
"""

import numpy as np

a1=15.67
a2=17.23
a3=0.75
a4=93.2

A=int(input("Input A: "))
Z=int(input("Input Z: "))

if A%2 == 1:
    a5=0
elif (A%2 == 0) and (Z%2 ==0):
    a5=12.0
else:
    a5=-12.0
    
B=a1*A - a2*(A**(2/3)) - a3*((Z**2)/(A**(1/3))) - a4*(((A-2*Z)**2)/(A))-(a5/(A**0.5))


print(B)
