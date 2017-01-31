#%%

import numpy
import bisect
import matplotlib.pyplot as plt

N = 50

a = numpy.zeros((N, N))
a[N / 2, N / 2] = 1
u = numpy.ones((N, N))

R = 50

ahist = []

t = 0.0
dts = []
for r in range(R):
    possibilities = []

    for i, j in zip(*numpy.where(a == 1)):
        for io, jo in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if i + io >= N or i + io < 0:
                continue

            if j + jo >= N or j + jo < 0:
                continue

            if a[i + io, j + jo] == 0:
                possibilities.append((u[i + io, j + jo], (i + io, j + jo)))

    rates, targets = zip(*possibilities)

    rsum = numpy.cumsum(rates)

    dt = numpy.random.exponential(1.0 / rsum[-1])

    r = numpy.random.rand() * rsum[-1]

    i = bisect.bisect_left(rsum, r)

    a[targets[i]] = 1

    t += dt

    dts.append(dt)

    plt.imshow(a)
    plt.show()

#%%

Xs = []
Ys = []

for i in range(len(ahist) - 1):
    for i, j in zip(*numpy.where(a == 1)):
        for io, jo in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if i + io >= N or i + io < 0:
                ignore = True
                break

            if j + jo >= N or j + jo < 0:
                ignore = True
                break

            if a[i + io, j + jo] == 0:
                possibilities.append((u[i + io, j + jo], (i + io, j + jo)))