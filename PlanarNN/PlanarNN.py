# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:22:07 2018

@author: gan0312
"""

# Package imports
import numpy as np
import matplotlib.pyplot as plt
from testCases_v2 import *
import sklearn
import sklearn.datasets
import sklearn.linear_model
from planar_utils import plot_decision_boundary, sigmoid, load_planar_dataset, load_extra_datasets

#%matplotlib inline

np.random.seed(1) # set a seed so that the results are consistent