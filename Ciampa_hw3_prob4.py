# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:16:32 2017

@author: Drew
"""

import numpy as np
import matplotlib.pyplot as plt

#Create an x array to set integration limit slices
x=np.arange(0,3.1,.1)

#Create a zero array to fill with integrated values
y=np.zeros(len(x))

#Define a function for the trapezoid rule
#input the function, limits of integration, and iterations
def trapezoid(f,a, b, n):
    h=(b-a)/n

    area = (f(a) + f(b))/2.0

    #Loop over the number of iterations to calculate the area
    for i in range(1, n):
        x = a + i*h;
        area += f(x)
    area = area*h

    return area

#Fill an array with y values for plotting the function
for j in range(len(x)):
    y[j]=trapezoid(lambda x:np.exp(x**2),0.,x[j],30)

#Plot our data
plt.figure(figsize=([10,6]))
plt.plot(x,y)
plt.xlim([0,3.1])
plt.xlabel("x")
plt.ylabel("E(x)")
plt.savefig("Ciampa_hw3_prob4.png",format='png')
