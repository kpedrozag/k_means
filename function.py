# -*- coding: utf-8 -*-
import numpy as np
import random as rd

def k_means(n_cent):
    dataset = np.loadtxt('cluster.txt', delimiter=';')
    # position of each centroid in dataset
    pos_cents = []
    while True:
        pos = rd.randint(0, dataset.shape[0] - 1)
        if pos not in pos_cents:
            pos_cents.append(pos)
            if len(pos_cents) == n_cent:
                break
    print("random position of centroids: ", pos_cents)
    # centroids
    cents = np.arange(2).reshape((1,2))
    for i in range(n_cent):
        cents = np.append(cents, [dataset[pos_cents[i]]], axis=0)
    cents = cents[1:]
    print("centroids: ", cents)
    # position of the centroid of each point
    cluster = np.array(0)
    for i in range(dataset.shape[0]):
        # if this position is not a centroid
        if dataset[i] not in cents:
            # save the euclidean distance
            dist = []
            # initial euclidean distance
            d_my_cent = np.power(dataset[0][0] - cents[0][0], 2)
            d_my_cent += np.power(dataset[0][1] - cents[0][1], 2)
            d_my_cent = np.sqrt(d_my_cent)
            # initial position
            pc = 50
            # calculate the distance from each point to each centroid
            for j in range(n_cent):
                val = np.power(dataset[i][0] - cents[j][0], 2)
                val += np.power(dataset[i][1] - cents[j][1], 2)
                val = np.sqrt(val)
                dist.append(val)
                # look for the min value of distance
                if val < d_my_cent:
                    d_my_cent = val + 0.0
                    pc = j
            #cluster.append(pc)
            cluster = np.append(cluster, pc)
        else:
            # -1 means this position is a centroid
            #cluster.append(-1)
            cluster = np.append(cluster, -1)
    cluster = cluster[1:]
    print(cluster)
    # position of the points binded to centroid
    #for i in range(n_cent):
    #    pec = np.where(cluster == i)
        


k_means(2)