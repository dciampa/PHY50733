# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 14:17:04 2017

@author: Drew
"""

import numpy as np
from random import random

#This is our function that we wish to integrate
def f(x):
    return ((x**(-.5))/(np.exp(x)+1))
    
N=1000000
count=0

#Taking a random number 0 to 1 and inputting it into the function. Doing this 1,000,000 times.
for i in range(N):
    x=random()
    count += f(x)

#From the textbook we know the area is equal to the counts under the loop divided by the number of sample points.
I=count/N
print(I)