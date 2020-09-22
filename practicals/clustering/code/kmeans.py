#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:53:41 2020

@author: dirk
"""
import numpy as np

def fit(X, k, alpha):
    # Set some samples as original means

    # Set two mu's to keep track if new and old change
    
    # loop until the mu's do not change

        
        # Asign new value to old value to be able to keep track of change
        # make sure to make a copy, else it is only a view on mu_new

        
        # Create an extra dimension of length k to store the distances
        # of the datapoints between X and mu_new
        # you can also make a for loop, but this is faster

        
        # Calculated the distance between X and mu_new

    
        # Assign classes 

        
        # Get new mu's using mean
        
    pass

def predict(X,mu):
    # get number of means

    
    # Create an extra dimension of length k to store the distances
    # of the datapoints between X and mu_new
    # you can also make a for loop, but this is faster

    
    # calculate the distance form samples to different mu and assign class
    # np.multiply gives a elementwise product (it squares every element)
    
    
    # Assign classes

    pass