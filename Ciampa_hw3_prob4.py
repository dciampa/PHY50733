# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:16:32 2017

@author: Drew
"""

import numpy as np

def simpson(f, a, b, n):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1, int(n/2 + 1)):
        k += 4*f(x)
        x += 2*h

    x = a + 2*h
    
    for i in range(1,int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)
    
print(simpson(lambda x:np.exp(x**2),0.,3.,100.))
