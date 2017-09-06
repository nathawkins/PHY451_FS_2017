#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:33:39 2017

@author: nathanielhawkins
"""

#Importing in the needed libraries
from numpy import genfromtxt
import numpy as np

#Reading in the data
channel1 = genfromtxt('osc_channel1.csv', delimiter = ',')
channel2 = genfromtxt('osc_channel2.csv' ,delimiter = ',')
voltages = np.reshape(channel2[:,1], (10000, -1))

#Concatenating the data into an array
all_data = np.concatenate((channel1, voltages), axis = 1)
all_data = np.reshape(all_data, (10000, 3))
all_data = all_data[:, 1:]

#Rescaling the data
all_data[:, 0]/=5000
all_data[:, 1]/=-1000

curr_un = []
volt_un = []


#Assinging unceratinty to both voltage and current
#Current uncertainty
for i in all_data[:, 0]:
    curr_un.append(0.02*i)
curr_un = np.array(curr_un)
curr_un = np.reshape(curr_un, (10000, -1))

#Voltage uncertainty
for i in all_data[:, 1]:
    volt_un.append(0.02*i)
volt_un = np.array(volt_un)
volt_un = np.reshape(volt_un, (10000, -1))

#Arranging it nicely
data_to_output = np.column_stack((all_data[:,0], curr_un))
data_to_output = np.column_stack((data_to_output, all_data[:, 1]))
data_to_output = np.column_stack((data_to_output, volt_un))

np.savetxt('osc_data_arranged.txt', data_to_output, delimiter = ',')

