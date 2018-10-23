# -*- coding: utf-8 -*-

from function import k_means
from k-means_scikit import run

K = range(1,10)

for k in K:
    print("centroids with", k, "clusters: ", k_means(k))

run()