import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#Read in our data and assign columns to x and y data.
filename="munich_temperatures_average_with_bad_data.txt"
data = np.genfromtxt(filename)
x=data[:,0]
y=data[:,1]

#Create a mask that removes any outliers.
mask=np.where((y>-50) & (y<50))[0]

#Apply the mask to our data arrays.
x_masked=x[mask]
y_masked=y[mask]

#Just plotting to make sure masking worked properly.
plt.plot(x_masked,y_masked,'.')
plt.show()

#Make our initial guesses for our fit.
guess_amplitude=int(input("guess_amplitude: "))
guess_phase=int(input("guess_phase: "))
guess_offset=int(input("guess_offset: "))

#Place the guesses into an array
p0=[guess_amplitude,guess_phase,guess_offset]

#Define a function that will be fit to our data.
def my_cos(t,a,b,c):
	return np.cos(2*np.pi*t + b)*a + c

#Use curve_fit to fit the function to the data using our initial guesses.
fit=curve_fit(my_cos,x_masked,y_masked,p0=p0)

#Create data using the first guess parameters.
data_first_guess=my_cos(x_masked,*p0)

#Create data using the curve_fit parameters.
data_fit=my_cos(x_masked,*fit[0])

#Print out the fitted parameters.
print(fit[0])
print('Average Temperature: ', np.mean(data_fit))
print('Coldest Day: ', np.min(data_fit))
print('Hottest Day: ', np.max(data_fit))



#Plot everything to see how it is fitted.
plt.plot(x_masked,y_masked,'.')
plt.xlim([2008,2012])
plt.plot(x_masked,data_fit,label='after fitting')
plt.plot(x_masked,data_first_guess,label='first guess')
plt.legend()
plt.show()
