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
x1 = X[:,0]
x2 = X[:,1]
inertias = []
K = range(2, 11)
for k in K:
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)

fig = plt.figure()
plt.plot(K, inertias, 'bx')
plt.grid(True)
plt.title('Elbow curve')