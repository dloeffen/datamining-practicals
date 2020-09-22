# Author: Dirk W.M. Loeffen
import numpy as np

def lse_fit(X,y):
    # add column of ones for the intercept
    ones = np.ones((len(X), 1))
    X = np.concatenate((ones, X), axis=1)

    # calculate the coefficients
    beta = np.dot(np.linalg.inv(np.dot(X.T, X)), np.dot(X.T, y))

    return beta


def lse_predict(X, theta):
    # add column of ones for the intercept
    ones = np.ones((len(X), 1))
    X = np.concatenate((ones, X), axis=1)
    
    # dot product between X and theta gives the prediction
    y_pred = np.dot(X,theta)
    return y_pred
