# Author: Dirk W.M. Loeffen
# Python file that implements a naive bayes classifier
import numpy as np
import utils
from operator import itemgetter
import pprint
from math import ceil

#TODO: hacky solution, implement something more robust

def fit_features(feature_set, feature_type, max_value=None, bin_width=1):
    if feature_type == 'binary':
        return utils.probability_binary(feature_set)
    elif feature_type == 'histogram':
        return utils.probability_histogram(feature_set, max_value, bin_width)
    else:
        print("Probability not implemented for feature type: {0}".format(feature_type))
        return


def fit(X, y, feature_types):
    # Implement a naive bayes classifier
    # Count number of features in X
    number_of_features = len(X.T)

    unique_classes = np.unique(y)
    
    # Create dictionary to store chances in
    chances = utils.probability_binary(y)

    max_value = np.max(X)

    # loop over number_of_features
    for unique_class in unique_classes:
        X_current = X[y==unique_class]
        chances["{0}_featureset".format(int(unique_class))] = dict()
        for i in range(number_of_features):
            feature_type = feature_types[i]
            current_feature_set = X_current[:,i] 
            chances["{0}_featureset".format(int(unique_class))][str(i)] = fit_features(current_feature_set, feature_type, max_value)

    return chances

def predict(X, model):
    # Implement the prediction of a naive bayes classifier
    
    # Get number of classes
    classes = [key for key in model.keys() if key.endswith('featureset')]

    # numpy array to store the class probabilities in
    y = np.zeros((len(X),len(classes)))

    for c in classes:
        class_num = c.split('_')[0]
        print("Class number: {0}".format(class_num))
        class_probabilities = model[c]
        features = class_probabilities.keys()
        y_feature = y[:,int(float(class_num))]
        y_feature += model[class_num]
        for key in features:
            print("Key: {0}".format(key))
            # numpy array with values of features
            feature_set = X[:,int(key)]
            feature_dict = class_probabilities[key]
            pprint.pprint(feature_dict)
            for index in range(len(feature_set)):
                value = str(ceil(feature_set[index]))
                if key == '1' and value == '0':
                    value = '1'
                max_key = max(feature_dict.keys(), key=lambda k: int(k))
                if key == '1' and int(value) > int(max_key):
                    value = max_key
                    
                y[index] +=  feature_dict[value]
    
    pprint.pprint(y)
    
    return np.argmax(y, axis=1)

