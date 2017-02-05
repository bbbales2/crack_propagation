#%%

import numpy
import os
import matplotlib.pyplot as plt

os.chdir('/home/bbales2/crack_propagation')

#%%

a = numpy.load('crack1.npy')
b = numpy.load('crack2.npy')

plt.imshow(a, interpolation = "NONE")
plt.gcf().set_size_inches((10, 10))
plt.show()

plt.imshow(b - a, interpolation = "NONE")
plt.gcf().set_size_inches((10, 10))
plt.show()

#%%

c = numpy.load('crack_grains.npy')
d = numpy.load('sample.npy')

plt.imshow(c)
plt.show()
