#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:55:53 2020

@author: dirk
"""
import numpy as np

def euclidian_distance(x,y):
    # Implement the euclidian distance using simple matrix operations
    return np.sqrt(np.sum(np.multiply(x-y,x-y)))

def random_float(min_value, max_value):
    return (max_value - min_value)*np.random.random() + min_value