# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:44:14 2017

@author: Drew
"""

import numpy as np

V=.001 #m^3
rho=6.022e28 #m^-3
theta=428 #K
N=1000
k=1.38e-23 #m^2 kg s^-2 K^-1

def f(x):
	return ((x**4) * np.exp(x))/((np.exp(x)-1)**2)

def cv(T):
	a=0.0
	b=(theta/T)
	h=(b-a)/N
    A1=9*V*rho*k*((T**3)/(theta**3))
	s=0.5*f(a) + 0.5*f(b)
	for k in range(1,N):
		s += f(a+k*h)
    C=h*(A1*s)
    print(C)
    return


cv(500)
