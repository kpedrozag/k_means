#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:02:45 2018

@author: ceisutb17
"""

import numpy as np
from scipy.spatial.distance import cdist
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris = load_iris()
x = np.loadtxt('cluster.txt', delimiter=';')

res = list()
n_cluster = range(2,10)
for n in n_cluster:
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(x)
    res.append(np.average(np.min(cdist(x, kmeans.cluster_centers_, 'euclidean'), axis=1)))

plt.plot(n_cluster, res)
plt.title('elbow curve')
plt.show()