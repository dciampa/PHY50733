# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:03:07 2017

@author: Drew
"""

import numpy as np

#definig the constants
a1=15.67
a2=17.23
a3=0.75
a4=93.2

#inputs for the values of A and Z
A=int(input("Input A: "))
Z=int(input("Input Z: "))

#if statement that will determine whether your values are even or odd.
#this changes the value for the a5 constant
if A%2 == 1:
    a5=0
elif (A%2 == 0) and (Z%2 ==0):
    a5=12.0
else:
    a5=-12.0
    
#the binding energy equation given on the homework
B=a1*A - a2*(A**(2/3)) - a3*((Z**2)/(A**(1/3))) - a4*(((A-2*Z)**2)/(A))-(a5/(A**0.5))

#pring the binding energy
print("The binding energy B is:",B)
#print the binding energy per nucleon
print("The binding energy per nucleon is:",B/A)
