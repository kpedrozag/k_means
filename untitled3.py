#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:39:01 2018

@author: ceisutb17
"""

from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import numpy as np

X = np.loadtxt('cluster.txt', delimiter=';')
distorsions = []
K = range(2, 10)
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    distorsions.append(kmeans.inertia_)

fig = plt.figure()
plt.plot(K, distorsions, 'bx-')
plt.grid(True)
plt.title('Elbow curve')