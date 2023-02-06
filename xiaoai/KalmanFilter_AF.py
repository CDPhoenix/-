# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 17:51:49 2023

@author: WANG Phoenix, Deparment of Mechanical Engineering, THE HONG KONG POLYTECHNIC UNIVERSITY
"""
import pandas as pd
import numpy as np
import cv2 as cv
import math
import matplotlib.pyplot as plt

path = './data.csv'
data = pd.read_csv(path)

class KalmanFilter:
    kf = cv.KalmanFilter(2,2)
    kf.measurementMatrix = np.array([[1,0],[0,1]],np.float32)
    kf.transitionMatrix = np.array([[1,0],[0,1]],np.float32)
    
    def predict(self,coordX,coordY):
        
        measured = np.array([[np.float32(coordX)],[np.float32(coordY)]])
        self.kf.correct(measured)
        predicted = self.kf.predict()
        x,y = predicted[0],predicted[1]
        return x[0],y[0]

datasetX = data['GDP_02']
datasetY = data['Rental Index']
kf = KalmanFilter()
length = len(data)
Xprediction = []
Xerror = []
Yprediction = []
Yerror = []

for i in range(length-1):
    x,y = kf.predict(datasetX[i],datasetY[i])
    x_error = abs((x-datasetX[i+1])/datasetX[i+1])
    y_error = abs((y-datasetY[i+1])/datasetY[i+1])
    Xprediction.append(x)
    Yprediction.append(y)
    Xerror.append(x_error)
    Yerror.append(y_error)

True_GDP = list(data['GDP_02'].values)
plt.figure()
plt.plot(True_GDP)
plt.plot(Xprediction)
plt.show()