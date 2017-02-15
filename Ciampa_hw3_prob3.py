# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 15:44:14 2017

@author: Drew
"""

import numpy as np
import matplotlib.pyplot as plt

V=.001 #m^3
rho=6.022e28 #m^-3
theta=428 #K
N=1000
K=1.38e-23 #m^2 kg s^-2 K^-1
y=np.zeros(200)
t=np.linspace(5,500,200)

#Define a function to integrate and calculate the heat capacity of a solid.
def cv(f, n, T):
    a=0.001     #Avoid starting at 0.0 as it will give NaN as an answer for the integral!
    b=(theta/T)   
    h = float(b - a) / n
    A1=9*V*rho*K*((T**3)/(theta**3))
    
    s = 0.0
    s += f(a)/2.0
    
    for i in range(1, n):
        s += f(a + i*h)
    s += f(b)/2.0
    
    return s * h *A1

#Loop through a bunch of temperatures and fill an array with their heat capacity.
for j in range(200):
    y[j]=cv(lambda x:((x**4) * np.exp(x))/((np.exp(x)-1)**2), N, t[j])
    
#print(y)
plt.figure(figsize=([10,6]))
plt.plot(t,y)
plt.xlabel('Temperature (K)')
plt.ylabel('Heat Capacity')
