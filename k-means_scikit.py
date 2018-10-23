#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:34:53 2018

@author: ceisutb17
"""

 # clustering dataset
# determine k using elbow method

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def run():
    X = np.loadtxt('cluster.txt', delimiter=';')
    
    # k means determine k
    inertias = []
    K = range(2,10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k).fit(X)
        kmeanModel.fit(X)
        inertias.append(kmeanModel.inertia_)
    
    # Do the maths for the slope of each straight line
    m = []
    for i in range(1, len(K)):
        mu = (inertias[i] - inertias[i-1]) / (K[i] - K[i-1])
        m.append(mu)
    
    # Do the maths for the substraction among the slope of each straight line
    # and the slope of the previous straight line
    dif_m = []
    for i in range(1, len(m)):
        dif = m[i] - m[i-1]
        dif_m.append(dif)
    
    elbow_line = max(dif_m)
    print( "La mayor diferencia entre pendientes es", elbow_line)
    
    for i in range(len(dif_m)):
        print("diferencia", i+1, ":", dif_m[i])
    
    """
    Se observa que la mayor diferencia se da en el valor de k=3
    """
    # Plot the elbow
    plt.plot(K, inertias, 'bx-')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia measurement')
    plt.title('The Elbow Method showing the optimal number of clusters\n')
    plt.grid(True)
    plt.show()
    
    # Plot the differences
    plt.plot(range(1, len(dif_m)+1), dif_m, 'bo-')
    plt.xlabel('pendiente')
    plt.ylabel('Diferencia')
    plt.grid(True)
    plt.title('Difference between a line and the previous line')
    plt.show()