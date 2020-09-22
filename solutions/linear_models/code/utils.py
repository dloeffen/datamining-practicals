#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:09:10 2020

@author: dirk
"""
import numpy as np

def sum_squared_errors(y1, y2):
    # Implement sum of squared errors
    diff = y1 - y2
    square = np.multiply(diff, diff)
    
    return np.sum(square)

def mean_squared_error(y1, y2):
    # Implement mean squared error
    return sum_squared_errors(y1,y2)/len(y1)

def root_mean_squared_error(y1, y2):
    # Implement root squared error
    return np.sqrt(mean_squared_error(y1,y2))