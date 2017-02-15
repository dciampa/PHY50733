# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:04:09 2017

@author: Drew
"""

import numpy as np
import matplotlib.pyplot as plt

filename="stm.txt"   #Set a variable for the filename
data = np.genfromtxt(filename)    #Import the data file using numpy function


plt.imshow(data)  #Simply plot the data with a color mapping to it
plt.colorbar()
plt.savefig("Ciampa_hw3_prob1.png", format='png')   #Save the PNG of the image
