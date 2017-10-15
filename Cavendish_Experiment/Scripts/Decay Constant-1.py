#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:44:22 2017

@author: stevenfromm
"""

import SpinlabCF as cf
import numpy as np
import matplotlib.pyplot as plt

name = '20171010-Cavendish-Trial'

dataFile = name + '.txt'

po = cf.PlotOptions(title='Free Oscillation Decay - No Large Lead Balls',
                    xlabel='Time (s)', ylabel='Angle (Not Callibrated) (mrad)',
                    fontfamily='Palatino',capsize=0,pt_fmt='r.')

data = cf.DataSet(dataFile)

start = np.where(data.X==1000)[0][0]
end = np.where(data.X==1800)[0][0]
print(start)

cf.DisplayData(data,po,saveFile='-'.join((name,'data.pdf')),errors=False)

data.X = data.X[start:end]
data.dX = data.dX[start:end]
data.Y = data.Y[start:end]
data.dY = data.dY[start:end]

def decay(t,theta0,A,b,omega1,phi):
    return theta0+A*np.exp(-b*t)*np.cos(omega1*t+phi)

def InitGuess(data):
    return (-30,31,0.001,0.03,0.05)

model = cf.UserModel('decay',decay,['theta0','A','b','w1','phi'],
                     'y=A*exp(-b*t)*cos(w1*t+phi)+theta0',InitGuess)

fit = cf.Fit(data,model)

fit.DisplayFit(po,errors=False,saveFile='-'.join((name,'fit.pdf')))

po.title = 'Residuals of Fit'
po.ylabel = 'Residuals y-y_fit (mrad - uncalibrated)'
fit.DisplayResiduals(po,errors=False,saveFile='-'.join((name,'res.pdf')))
print(fit.Results())
