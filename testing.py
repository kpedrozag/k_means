#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:28:02 2018

@author: ceisutb17
"""

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

X = np.loadtxt('cluster.txt', delimiter=';')

# k means determine k

kmeanModel = KMeans(n_clusters=2).fit(X)
kmeanModel.fit(X)

print(kmeanModel.cluster_centers_)