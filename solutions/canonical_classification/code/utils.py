# Author: Dirk W.M. Loeffen
# file containing different utilities that are
# useful for this exercise

import numpy as np

def probability_binary(x):
    # given a entry of x calculate its chance for being randomly
    # picked in x
    
    # get number of elements in x
    n = len(x)
    n_unique = np.unique(x)

    # create dict to store bins in
    chances = dict()

    for unique in n_unique:
        n_entry  = len(x[x==unique])
        chances[str(int(unique))] = n_entry/n

    return chances

def probability_histogram(x, max_value, bin_width):
    # get total number of elements
    total_elements = len(x)
    # get number of bins
    number_of_bins = int(max_value//bin_width + 1)

    # create dict to store bins in
    chances = dict()

    for bin_number in range(1,number_of_bins):
        elements_current_bin = x[np.where((x>=(bin_number-1)*bin_width) & (x<bin_number*bin_width))]
        number_current_elements = len(elements_current_bin)
        chances[str(bin_number*bin_width)] = number_current_elements/total_elements

    return chances
