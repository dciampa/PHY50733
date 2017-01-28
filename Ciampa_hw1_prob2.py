import numpy as np

#Input the period of orbit.
T=int(input("Value of T (Period): "))

G=6.67e-11 #Constant m^3 kg^-1 s^-2
M=5.97e24  #Mass in kg
R=6371000  #Radius in meters

#Altitude equation
h=(((G*M*(T**2))/(4*(np.pi**2)))**(1/3))-R

print(h)