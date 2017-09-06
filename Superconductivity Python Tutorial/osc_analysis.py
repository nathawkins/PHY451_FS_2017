#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:04:54 2017

@author: nathanielhawkins
"""

#Importing the Spinlab file
import SpinlabCF as cf

#Create DataSet Object
data = cf.DataSet('osc_data_arranged.txt', delim =',')

#Make fit
fit = cf.Fit(data, cf.Fit.Linear)
fit.DisplayFit()
print(fit.Results())

#This gives a slope of 0.974 which is approximately 1
