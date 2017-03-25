import fitsio
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


data=fitsio.FITS('~/Downloads/sdss.fits')

cut = data[1].where('GLAT >-1 && GLAT<1 && GLON < 185 && GLON > 175')
subset=data[1][cut]
print(subset[0]['FE_H'])
print(subset[0]['O_FE'])
print(subset[0]['FE_H_ERR'])
print(subset[0]['O_FE_ERR'])

Fe=[]
O=[]
Fe_err=[]
O_err=[]

for i in range(len(subset)):
	Fe.append(subset[i]['FE_H'])
	O.append(subset[i]['O_FE'])
	Fe_err.append(subset[i]['FE_H_ERR'])
	O_err.append(subset[i]['O_FE_ERR'])

Fe=np.array(Fe)
O=np.array(O)
Fe_err=np.array(Fe_err)
O_err=np.array(O_err)

#Create a mask that removes any outliers.
mask=np.where((Fe >-1) & (Fe < 1) & (O>-1) & (O<1))[0]

#Apply the mask to our data arrays.
O_masked=O[mask]
Fe_masked=Fe[mask]
O_err_masked=O_err[mask]
Fe_err_masked=Fe_err[mask]

print("max Fe: ", max(Fe))
print("min Fe: ",min(Fe))
print("max O: ",max(O))
print("min O: ",min(O))

plt.plot(O_masked,Fe_masked,'.')
plt.show()

#LINEAR FIT

#Make our initial guesses for our fit.
guess_m=float(input("guess_m: "))
guess_b=float(input("guess_b: "))

#Place the guesses into an array
p0=[guess_m,guess_b]

#Define a function that will be fit to our data.
def linear(x,m,b):
	return m*x + b

#Use curve_fit to fit the function to the data using our initial guesses.
fit=curve_fit(linear,O_masked,Fe_masked,p0=p0)

#Create data using the first guess parameters.
data_first_guess=linear(O_masked,*p0)

#Create data using the curve_fit parameters.
data_fit=linear(O_masked,*fit[0])

#Plot everything to see how it is fitted.
plt.plot(O_masked,Fe_masked,'.')
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.plot(O_masked,data_fit,label='after fitting')
plt.plot(O_masked,data_first_guess,label='first guess')
plt.legend()
plt.show()

#QUADRATIC FIT

#Make our initial guesses for our fit.
guess_a=float(input("guess_a: "))
guess_b=float(input("guess_b: "))
guess_c=float(input("guess_c: "))

#Place the guesses into an array
p01=[guess_a,guess_b,guess_c]

#Define a function that will be fit to our data.
def quad(x,a,b,c):
	return a*x**2 + b*x + c

#Use curve_fit to fit the function to the data using our initial guesses.
fit1=curve_fit(quad,O_masked,Fe_masked,p0=p01)

#Create data using the first guess parameters.
data_first_guess1=quad(O_masked,*p01)

#Create data using the curve_fit parameters.
data_fit1=quad(O_masked,*fit1[0])

#Plot everything to see how it is fitted.
plt.plot(O_masked,Fe_masked,'.')
plt.xlim([-1,1])
plt.ylim([-1,1])
plt.plot(O_masked,data_first_guess1,'r.',label='first guess')
plt.plot(O_masked,data_fit1,label='after fitting')
plt.legend()
plt.show()
