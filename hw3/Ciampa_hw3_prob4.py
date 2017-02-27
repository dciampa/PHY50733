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
    s = (f(a) + f(b))/2.0

    #Loop over the number of iterations to calculate the area
    for i in range(1, n):
        x = a + i*h;
        s += f(x)

    return s*h

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