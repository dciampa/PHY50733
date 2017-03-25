import fitsio
import matplotlib.pyplot as plt
import numpy as np
data=fitsio.FITS('~/Downloads/sdss.fits')
print(data)
print(data[1])

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

#print(len(subset))#913

for i in range(len(subset)):
	Fe.append(subset[i]['FE_H'])
	O.append(subset[i]['O_FE'])
	Fe_err.append(subset[i]['FE_H_ERR'])
	O_err.append(subset[i]['O_FE_ERR'])


print(max(Fe))
print(min(Fe))
print(max(O))
print(min(O))
plt.plot(O,Fe,'.')
plt.show()