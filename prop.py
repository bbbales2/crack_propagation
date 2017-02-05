#%%

import numpy
import bisect
import matplotlib.pyplot as plt

N = 50

a = numpy.zeros((N, N))
a[N / 2, N / 2] = 1
u = numpy.ones((N, N))
u[:, :N / 2] = 0.5

R = 500

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

    rr = numpy.random.rand() * rsum[-1]

    i = bisect.bisect_left(rsum, rr)

    a[targets[i]] = 1

    t += dt

    dts.append(dt)

    if r % 10 == 0:
        ahist.append(a.copy())
        plt.imshow(a, interpolation = 'NONE')
        plt.show()

#%%

Xs = []
Ys = []

for t in range(len(ahist) - 1):
    print t
    growth = ahist[t + 1] - ahist[t]
    
    for i in range(N):
        for j in range(N):
    #for i, j in zip(*numpy.where(a == 1)):
            neighbors = []
            ignore = False
            
            for io, jo in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if i + io >= N or i + io < 0:
                    ignore = True
                    break
    
                if j + jo >= N or j + jo < 0:
                    ignore = True
                    break
                
                neighbors.append(ahist[t][i + io, j + jo])
                
            if ignore:
                continue
    
            neighbors = tuple(neighbors)
        
        #if neighbors is not (1, 1, 1, 1):
            Xs.append(neighbors)
            Ys.append(growth[i, j])
            
    #plt.imshow(growth)
    #plt.show()
            
#%%
            
import sklearn.linear_model

lr = sklearn.svm.SVC(class_weight = 'balanced')
lr.fit(Xs, Ys)

#%%

for t in range(len(ahist) - 1):
    growth = ahist[t + 1] - ahist[t]
    
    Xs = []
    
    for i in range(1, N - 1):
        for j in range(1, N - 1):
    #for i, j in zip(*numpy.where(a == 1)):
            neighbors = []
            ignore = False
            
            for io, jo in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if i + io >= N or i + io < 0:
                    ignore = True
                    break
    
                if j + jo >= N or j + jo < 0:
                    ignore = True
                    break
                
                neighbors.append(ahist[t][i + io, j + jo])
                
            if ignore:
                continue
    
            neighbors = tuple(neighbors)
        
        #if neighbors is not (1, 1, 1, 1):
            Xs.append(neighbors)
            #Ys.append(growth[i, j])
            
    pgrowth = lr.predict(Xs)[:]
    
    pgrowth = numpy.pad(pgrowth.reshape((N - 2, N - 2)), 1, mode = 'edge')
    
    plt.imshow(pgrowth)
    plt.show()
                