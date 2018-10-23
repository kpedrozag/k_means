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
    #print("random position of centroids: ", pos_cents)
    # centroids
    cents = np.arange(2).reshape((1,2))
    for i in range(n_cent):
        cents = np.append(cents, [dataset[pos_cents[i]]], axis=0)
    cents = cents[1:]
    # print("centroids: ", cents)
    # position of the centroid of each point
    it=0
    for loop in range(1000):
        cluster = np.array(0)
        for i in range(dataset.shape[0]):
            # if this position is not a centroid
            #if True:
            #if dataset[i] not in cents:
            # save the euclidean distance
            dist = []
            # calculate the distance from each point to each centroid
            for j in range(n_cent):
                val = np.power(dataset[i][0] - cents[j][0], 2)
                val += np.power(dataset[i][1] - cents[j][1], 2)
                val = np.sqrt(val)
                dist.append(val)
                
            # initial euclidean distance
            #d_my_cent = np.power(dataset[0][0] - cents[0][0], 2)
            #d_my_cent += np.power(dataset[0][1] - cents[0][1], 2)
            #d_my_cent = np.sqrt(d_my_cent)
            # initial position
            d_my_cent = dist[0]
            pc = 0
            for j in range(len(dist)):
                # look for the min value of distance
                if dist[j] < d_my_cent:
                    d_my_cent = dist[j]
                    # save the position of the centroid in the centroids list
                    pc = j
            cluster = np.append(cluster, pc)
        #else:
            # -1 means this position is a centroid
            #cluster.append(-1)
            #cluster = np.append(cluster, -1)
        cluster = cluster[1:]
        
        #print(cluster)
        #for i in range(n_cent):
        #    print(cluster[pos_cents[i]])
        # position of the points binded to each centroid
        
        # array of temporal centroids
        temp_cents = np.copy(cents)
        
        # for each value in cents
        for i in range(n_cent):
            # positions of all the points binded to a centroid
            pec = np.where(cluster == i)[0]
            
            # coordinate x and y of the new centroids
            sumax1 = np.int64()
            sumax2 = np.int64()
            
            # do the maths for calculate the new centroids
            for pos in pec:
                sumax1 += dataset[pos][0]
                sumax2 += dataset[pos][0]
            sumax1 = sumax1 / pec.shape[0]
            sumax2 = sumax2 / pec.shape[0]
            
            # reassignment of the centroids in the array 
            # of temporal (new) centroids
            temp_cents = np.array((sumax1, sumax2))
        
        # if the new centroids are equal to the previous centroids
        #flag = np.array_equal(cents, temp_cents)
        #if flag:
            # the algorithms to obtain the centroids has finished.
        #    break
    
    return(cents)
