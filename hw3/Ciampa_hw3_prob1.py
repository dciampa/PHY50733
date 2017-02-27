import numpy as np
import matplotlib.pyplot as plt
filename="stm.txt"
data = np.genfromtxt(filename)

plt.imshow(data)
plt.colorbar()
plt.savefig("test.png",format='png')