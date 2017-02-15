# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 09:08:20 2017

@author: Drew
"""

import numpy as np

a=float(input("Input your value of a: "))
b=float(input("Input your value of b: "))
c=float(input("Input your value of c: "))

#a=.001
#b=1000
#c=.001

d=np.sqrt(b**2 -(4*a*c))

xplus=(-b + d)/(2*a)
xminus=(-b - d)/(2*a)

print("Root 1a w/ addition: ", xplus) #good
print("Root 1b w/ subtraction: ", xminus)

xplus2=(2*c)/(-b + d)
xminus2=(2*c)/(-b - d)

print("Root 2a w/ addition: ", xplus2)
print("Root 2b w/ subtraction: ", xminus2) #good

print("The addition of a negative number and the positive number with nearly equal absolute values produces rounding errors.")
print("Utilizing both methods and only using like sign operations, we get accurate roots.")

print("Root 1: ", xminus)
print("Root 2: ", xminus2)

print("The correct roots are -1e-6 and -1e6")