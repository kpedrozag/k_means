#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 10:28:02 2018

@author: ceisutb17
"""

import numpy as np

a = np.arange(2).reshape((1,2))
a = np.append(a, [[1,1]], axis=0)
print(a)