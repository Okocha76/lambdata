"""
utility functions for working with DataFrames
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import seaborn as sns

class FullName:
    '''
    Gives a full name.
    '''
    def __init__(self, first, middle, last):
        self.first = 'John'
        self.middle = 'Fitzgerald'
        self.last = 'Kennedy'
    
    def what_name(self):
        print(f'My full name is {self.first} {self.middle} {self.last}.')


def lazy_sqrt(x):
    """Takes x and returns square root"""
    return x**0.5

def builtin_sqrt(x):
    """Uses built in math library to get square root"""
    from math import sqrt
    return sqrt(x)

def newton_sqrt1(x):
    """"Return the square root of x using Newton's Method"""
    val = x
    while True:
        last = val
        val = (val + x / val) * 0.5
        if abs(val - last) < 1e-9:
            break
    return val

def confusion_plot(y_true, y_pred, cmap='viridis'):
    """
    Plots a confusion matrix using Seaborn.
    """
    table = pd.DataFrame(confusion_matrix(y_true, y_pred))
    return sns.heatmap(table, annot=True, fmt='d', cmap=cmap)


def three_way_split(X, train_size=0.8):
    '''
    Perform train, test, val split.
    '''
    train, test = train_test_split(X)
    train, val = train_test_split(train)
    return train, test, val