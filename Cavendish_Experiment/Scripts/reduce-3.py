#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:36:34 2017

@author: stevenfromm
"""

import numpy as np

inFile = "../Raw Data/20171010-Evening/20171010_cavendish_trial.txt"

t,angle = np.loadtxt(inFile, delimiter='\t',unpack=True)

dt = [0.001 for i in range(len(t))]
dangle = [0.1 for i in range(len(angle))]

data = np.array((t[1:],dt[1:],angle[1:],dangle[1:])).T

np.savetxt('20171010-Cavendish-Trial.txt',data,
           fmt='%.6f',delimiter='\t')