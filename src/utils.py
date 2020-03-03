#! -*- coding: utf-8 -*-

import math
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.metrics import auc

def array_rmse(array_a,array_b):
    return np.sqrt(np.mean(np.power(array_a-array_b,2)))

def non_negetive(X,Y):
    X   = np.array(X)
    length = X.shape[1] 
    W   = np.array([0.1]*length)
    Y   = np.array(Y).reshape(-1,1)
    X_A = np.dot(X.T,X)
    X_Y = np.dot(X.T,Y)
    W_old = W.copy()
    for j in range(100):
        Fenmu = np.dot(X_A,W)
        # 更新W
        for i in range(length):
            W[i] = float(W[i]*X_Y[i])/(Fenmu[i]+10**-6)
        if array_rmse(W,W_old)<10**-6:
            print("iteration = %d, rmse=%f, has  convergenced"%(j,array_rmse(W,W_old)))
            break
        W_old = W.copy()
        
    return W

def gradient_truncation(X,Y):
    X   = np.array(X)
    length = X.shape[1] 
    W   = np.array([0.1]*length).reshape(-1,1)
    Y   = np.array(Y).reshape(-1,1)
    X_A = np.dot(X.T,X)
    X_Y = np.dot(X.T,Y)
    W_old = W.copy()
    alpha = 0.0000005 # how to choose the learning rate is a question
    for j in range(3):
        descent = np.dot(X_A,W) - X_Y
        W = W - alpha*descent
        W = (W + abs(W)) / 2
        if array_rmse(W,W_old)<10**-6:
            print("iteration = %d, rmse=%f, has  convergenced"%(j,array_rmse(W,W_old)))
            break
        W_old = W.copy()
    W_list = []
    for i in range(len(W)):
        W_list.append(W[i][0])
    return np.array(W_list)

def RMSE(label_list,predict_list):
    label_list         = np.array(label_list)
    predict_list       = np.array(predict_list)
    squared_deviation  = np.power(label_list -predict_list , 2)
    return 0.5*np.sqrt(np.mean(squared_deviation))

# calcuate auc
def new_metric(tdf,seqnum_columns,y_label):
    true_label = list(tdf[y_label])
    auc =[]
    for colums_name in seqnum_columns:
        pred_label = list(tdf[colums_name])
        fpr, tpr, thresholds = metrics.roc_curve(true_label, pred_label, pos_label=1)
        value = metrics.auc(fpr, tpr)
        auc.append(value)
    return pd.DataFrame({"method":seqnum_columns,"metric_auc":auc})