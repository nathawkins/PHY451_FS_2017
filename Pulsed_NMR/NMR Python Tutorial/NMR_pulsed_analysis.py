#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:43:07 2017

@author: nathanielhawkins
"""
#Importing libraries for use in code
import SpinlabCF as cf
import numpy as np

#Creating dataset object using cf template
data = cf.DataSet('nmr_data.txt', headers = True)

#Defining the columns needed for analyzing the data
data.X = data['Delay Time']
data.dX = np.zeros(data.N)
data.Y = data['Amplitude']
data.dY = 0.05 * data.Y 

#Fitting the data and plotting the results
fit = cf.Fit(data, cf.Fit.ExpDecay)
fit.DisplayFit()
fit.DisplayResiduals()
print(fit.Results())

#Performing the same thing except using the edited version of the data that
#removes the first troublesome point seen in the residuals plot

#Creating dataset object using cf template
data = cf.DataSet('nmr_data_edited.txt', headers = True)

#Defining the columns needed for analyzing the data
data.X = data['Delay Time']
data.dX = np.zeros(data.N)
data.Y = data['Amplitude']
data.dY = 0.05 * data.Y 

#Fitting the data and plotting the results
fit = cf.Fit(data, cf.Fit.ExpDecay)
fit.DisplayFit()
fit.DisplayResiduals()
print(fit.Results())