# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 22:04:09 2017

@author: Drew
"""

import numpy as np
import matplotlib.pyplot as plt
filename="stm.txt"
data = np.genfromtxt(filename)

plt.imshow(data)
plt.colorbar()