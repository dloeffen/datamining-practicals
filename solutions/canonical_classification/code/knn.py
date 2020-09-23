# author: Dirk W.M. Loeffen
import numpy as np
import scipy as sp

def predict(X_train, X_test, y_train, k):
    """
    get the target values from the k nearest neighbors
    Parameters
    ----------
    X_train : numpy.ndarray
        numpy array containing training samples
    X_test : numpy.ndarray
        numpy array containing test samples
    y_train : numpy.ndarray
        numpy array containing training targets
    k : int
        number of neighbors to account for (preferably odd)
    Returns
    -------
    y_predic : numpy.ndarray
        numpy array containing predicted targets
    """
    # Create 3D matrix where the second dimension is the number of 
    # samples in X and the third dimension is the number of features
    # this has to be like this because now the last two axes of X_three
    # and X are the same and can be subtracted easily
    X_three = np.repeat(X_train[:, :, None], len(X_test), axis=2)
    X_three = np.swapaxes(X_three, 1, 2)
    
    # Subtract features of samples from 3D matrix
    X_subtract = X_three - X_test
    
    # Square, sum, square root, to get L2 norm
    X_l2 = np.sqrt(np.sum(np.multiply(X_subtract, X_subtract), axis = 2))
    
    # Get indices of the smallest
    # mind that argpartition does not sort, instead use np.argsort if wanted
    X_idx_k = np.argpartition(X_l2, k, axis=0)[:k, :]
    target_size = X_idx_k.shape
    
    # Get values and reshape
    y_k = y_train[X_idx_k.flatten()]
    y_k = y_k.reshape(target_size)
    
    return np.swapaxes(sp.stats.mode(y_k)[0], 0, 1)
