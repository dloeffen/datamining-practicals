#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:53:41 2020

@author: dirk
"""
import numpy as np

def fit(X, k, alpha):
    # Set some samples as original means
    number_of_samples = X.shape[0]
    idxs = np.random.randint(0, number_of_samples, k)
    mu_start = X[idxs]
    
    # Set two mu's to keep track if new and old change
    mu_old = np.asarray([[0,0],[0,0],[0,0]])
    mu_new = mu_start
    
    # loop until the mu's do not change
    while(~np.all(mu_old==mu_new)):
        
        # Asign new value to old value to be able to keep track of change
        # make sure to make a copy, else it is only a view on mu_new
        mu_old = mu_new.copy()
        
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

    return mu_new

def predict(X,mu):
    # get number of means
    k = len(mu)
    
    # Create an extra dimension of length k to store the distances
    # of the datapoints between X and mu_new
    # you can also make a for loop, but this is faster
    X_k_dimensions = np.repeat(X[:,:,None], k, axis=2)
    X_k_dimensions = np.swapaxes(X_k_dimensions, 1, 2)
    
    # calculate the distance form samples to different mu and assign class
    # np.multiply gives a elementwise product (it squares every element)
    X_minus = X_k_dimensions - mu
    X_distance = np.sqrt(np.sum(np.multiply(X_minus, X_minus), axis=2))
    
    # Assign classes
    classes = np.argmin(X_distance, axis=1)
    
    return classes