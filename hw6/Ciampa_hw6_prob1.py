# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:31:43 2017

@author: Drew
"""

import matplotlib.pyplot as plt
import numpy as np


g = 9.81  #m/s^2
l =0.11

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N
theta=-176

tpoints = np.arange(a,b,h)
thetapoints = []

def f(r,t):
    theta = r[0]
    omega = r[1]
    dtheta = omega
    domega = -g/l*np.sin(theta)
    return np.array([dtheta,domega],float)

#r = np.array([-176/180*pi,0],float)
r = np.array([theta*np.pi/180,0],float)
for t in tpoints:
    thetapoints.append(r[0])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6


thetapoints = 180/np.pi * np.array(thetapoints)
plt.plot(tpoints,thetapoints)
#plt.plot(tpoints,ypoints)
plt.xlabel("t")
plt.ylabel("theta")
plt.show()

