# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:18:24 2020

@author: Tanmay Thakur
"""
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler


data = pd.read_csv('features.csv')

input_data = data.drop(['Date','Time'], axis = 1).values

T = 60 
D = input_data.shape[1]
N = len(input_data) - T 

Ntrain = len(input_data) * 2 // 3
scaler = StandardScaler()
scaler.fit(input_data[:Ntrain + T - 1])
input_data = scaler.transform(input_data)

X_train = np.zeros((Ntrain, T, D))
Y_train = np.zeros((Ntrain, D))

for t in range(Ntrain):
  X_train[t, :, :] = input_data[t:t+T]
  Y_train[t] = input_data[t+T]
  
print(X_train.shape, Y_train.shape)