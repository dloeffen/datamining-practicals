#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:53:41 2020

@author: dirk
"""
import numpy as np
import utils

def fit(X, k, alpha):
    # Set some samples as original means
    number_of_samples = X.shape[0]
    idxs = np.random.randint(0, number_of_samples, k)
    mu_start = X[idxs]
    print("mu start: \n{0}\n".format(mu_start))
    
    # Set two mu's to keep track of the change
    # and asign a high value to change
    change = 99999
    mu_old = np.asarray([[0,0],[0,0],[0,0]])
    mu_new = mu_start
    print("mu new: \n{0}\n".format(mu_new))
    
    count = 0
    # loop until change is smaller than alpha
    while(~np.all(mu_old==mu_new)):
        count+=1
        
        # Asign new value to old value to be able to keep track of change
        # make sure to make a copy, else it is only a view on mu_new
        mu_old = mu_new.copy()
        print("mu old (loop {0}): \n{1}\n".format(count, mu_old))
        
        # Create an extra dimension of length k to store the distances
        # of the datapoints between X and mu_new
        # you can also make a for loop, but this is faster
        X_k_dimensions = np.repeat(X[:,:,None], k, axis=2)
        X_k_dimensions = np.swapaxes(X_k_dimensions, 1, 2)
        
        # Calculated the distance between X and mu_new
        X_minus = X_k_dimensions - mu_new
        X_distance = np.sqrt(np.sum(np.multiply(X_minus, X_minus), axis=2))
    
        # Assign classes 
        classes = np.argmin(X_distance, axis=1)
        
        # Get new mean
        for i in range(k):
            mu_new[i] = np.mean(X[classes==i], axis=0)
        print("mu new (loop {0}): \n{1}\n".format(count, mu_new))
        
        print("mu new and old the same: \n{0}\n".format(np.all(mu_old==mu_new)))

    return mu_new

def predict(X,mu):
    # calculate the distance form samples to different mu and assign class
    
    pass