from random import random
import numpy as np
import matplotlib.pyplot as plt

#Constants
h=1.0
tmax=20000
NBi209=0
NPb209=0
NTl209=0
NBi213=10000

#Probability of decay
pBi213=1 - 2**(-h/(46*60.))
pPb209=1 - 2**(-h/(3.3*60.))
pTl209=1 - 2**(-h/(2.2*60.))

#Lists to fill for each element
Tl209points=[]
Pb209points=[]
Bi209points=[]
Bi213points=[]
tpoints = np.arange(0.0,tmax,h)

for t in tpoints:
		#Each time through the loop, the amount of each element will be updated
        Tl209points.append(NTl209)
        Pb209points.append(NPb209)
        Bi209points.append(NBi209)
        Bi213points.append(NBi213)

        #Working from the bottom up, this analyzes if the Pb209 will decay into Bi209
        for i in range(NPb209):
                if random()<pPb209:
                        NPb209 -= 1
                        NBi209 += 1

        #Next we see if the Tl209 will decay into Pb209
        for i in range(NTl209):
                if random()<pTl209:
                        NTl209 -= 1
                        NPb209 += 1

        #Finally, we see which path the Bi213 will decay into. The first loop will only involve this condition.
        #After the first loop, the previous two conditions will become important.
        for i in range(NBi213):
                if random()<pBi213:
                        NBi213 -= 1
                        if random()<0.9791:
                                NPb209 += 1
                        else:
                                NTl209 += 1

#Make a graph of all the abundances
plt.plot(tpoints,Tl209points,label='Tl209')
plt.plot(tpoints,Pb209points,label='Pb209')
plt.plot(tpoints,Bi209points,label='Bi209')
plt.plot(tpoints,Bi213points,label='Bi213')
plt.legend()
plt.xlabel("Time")
plt.ylabel("Number of atoms")
plt.savefig("test.png",format='png')


#Write the element amounts to a txt file
file = open("testfile.txt","w")
file.write("Bi 213:" + "\t" + "Tl 209:" + "\t" + "Pb 209:" + "\t" + "Bi 209:" + "\n")
for i in range(len(tpoints)):
        file.write(str(Bi213points[i]) + "\t" + str(Tl209points[i]) + "\t" + str(Pb209points[i]) + "\t" + str(Bi209points[i]) + "\n")
        #file.write('{Bi213[i]}\t{Tl209[i]}\t{Pb209[i]}\t{Bi209[i]}\n'.format(l))
file.close()
