# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 14:22:07 2018

@author: gan0312
"""

# Package imports

from testCases_v2 import *
import matplotlib.pyplot as plt
import sklearn
import sklearn.datasets
import sklearn.linear_model
from planar_utils import plot_decision_boundary, load_planar_dataset, load_extra_datasets
from NNBlueprint import *

#%matplotlib inline

np.random.seed(1) # set a seed so that the results are consistent
#==============================================================================
# X, Y = load_planar_dataset()
# # Visualize the data:
# plt.scatter(X[0, :], X[1, :], c=Y, s=40, cmap=plt.cm.Spectral);
# 
# ### START CODE HERE ### (≈ 3 lines of code)
# shape_X = X.shape
# shape_Y = Y.shape
# m = X.shape[1]  # training set size
# ### END CODE HERE ###
# 
# print ('The shape of X is: ' + str(shape_X))
# print ('The shape of Y is: ' + str(shape_Y))
# print ('I have m = %d training examples!' % (m))
# # Train the logistic regression classifier
# clf = sklearn.linear_model.LogisticRegressionCV();
# clf.fit(X.T, Y.T);
# # Plot the decision boundary for logistic regression
# plot_decision_boundary(lambda x: clf.predict(x), X, Y)
# plt.title("Logistic Regression")
# 
# # Print accuracy
# LR_predictions = clf.predict(X.T)
# print ('Accuracy of logistic regression: %d ' % float((np.dot(Y,LR_predictions) + np.dot(1-Y,1-LR_predictions))/float(Y.size)*100) +
#        '% ' + "(percentage of correctly labelled datapoints)")
# 
#==============================================================================
#==============================================================================
# X_assess, Y_assess = layer_sizes_test_case()
# (n_x, n_h, n_y) = layer_sizes(X_assess, Y_assess)
# print("The size of the input layer is: n_x = " + str(n_x))
# print("The size of the hidden layer is: n_h = " + str(n_h))
# print("The size of the output layer is: n_y = " + str(n_y))
# 
# # GRADED FUNCTION: initialize_parameters
# 
# 
# 
# n_x, n_h, n_y = initialize_parameters_test_case()
# 
# parameters = initialize_parameters(n_x, n_h, n_y)
# print("W1 = " + str(parameters["W1"]))
# print("b1 = " + str(parameters["b1"]))
# print("W2 = " + str(parameters["W2"]))
# print("b2 = " + str(parameters["b2"]))
# 
# # GRADED FUNCTION: forward_propagation
# # GRADED FUNCTION: forward_propagation
# 
# 
# 
# X_assess, parameters = forward_propagation_test_case()
# A2, cache = forward_propagation(X_assess, parameters)
# 
# # Note: we use the mean here just to make sure that your output matches ours. 
# print(np.mean(cache['Z1']) ,np.mean(cache['A1']),np.mean(cache['Z2']),np.mean(cache['A2']))
# 
# # GRADED FUNCTION: compute_cost
# 
# A2, Y_assess, parameters = compute_cost_test_case()
# 
# print("cost = " + str(compute_cost(A2, Y_assess, parameters)))
# 
# # GRADED FUNCTION: backward_propagation
# 
# parameters, cache, X_assess, Y_assess = backward_propagation_test_case()
# 
# grads = backward_propagation(parameters, cache, X_assess, Y_assess)
# print ("dW1 = "+ str(grads["dW1"]))
# print ("db1 = "+ str(grads["db1"]))
# print ("dW2 = "+ str(grads["dW2"]))
# print ("db2 = "+ str(grads["db2"]))
# 
# # GRADED FUNCTION: update_parameters
# 
# 
# parameters, grads = update_parameters_test_case()
# parameters = update_parameters(parameters, grads)
# 
# print("W1 = " + str(parameters["W1"]))
# print("b1 = " + str(parameters["b1"]))
# print("W2 = " + str(parameters["W2"]))
# print("b2 = " + str(parameters["b2"]))
# 
# # GRADED FUNCTION: nn_model
# 
#==============================================================================
#==============================================================================
# X_assess, Y_assess = nn_model_test_case()
# parameters = nn_model(X_assess, Y_assess, 4, num_iterations=10000, print_cost=True)
# print("W1 = " + str(parameters["W1"]))
# print("b1 = " + str(parameters["b1"]))
# print("W2 = " + str(parameters["W2"]))
# print("b2 = " + str(parameters["b2"]))
# 
# 
# 
# 
# 
# parameters, X_assess = predict_test_case()
# 
# predictions = predict(parameters, X_assess)
# print("predictions mean = " + str(np.mean(predictions)))
#==============================================================================





#==============================================================================
# # Build a model with a n_h-dimensional hidden layer
# parameters = nn_model(X, Y, n_h = 4, num_iterations = 10000, print_cost=True)
# # Plot the decision boundary
# plot_decision_boundary(lambda x: predict(parameters, x.T), X, Y)
# plt.title("Decision Boundary for hidden layer size " + str(4))
# # Print accuracy
# predictions = predict(parameters, X)
# print ('Accuracy: %d' % float((np.dot(Y,predictions.T) + np.dot(1-Y,1-predictions.T))/float(Y.size)*100) + '%')
# 
#==============================================================================
# This may take about 2 minutes to run
#==============================================================================
# 
# plt.figure(figsize=(16, 32))
# hidden_layer_sizes = [1, 2, 3, 4, 5, 20]
# for i, n_h in enumerate(hidden_layer_sizes):
#     plt.subplot(5, 2, i+1)
#     plt.title('Hidden Layer of size %d' % n_h)
#     parameters = nn_model(X, Y, n_h, num_iterations = 5000)
#     plot_decision_boundary(lambda x: predict(parameters, x.T), X, Y)
#     predictions = predict(parameters, X)
#     accuracy = float((np.dot(Y,predictions.T) + np.dot(1-Y,1-predictions.T))/float(Y.size)*100)
#     print ("Accuracy for {} hidden units: {} %".format(n_h, accuracy))
#==============================================================================
    
noisy_circles, noisy_moons, blobs, gaussian_quantiles, no_structure = load_extra_datasets()

datasets = {"noisy_circles": noisy_circles,
            "noisy_moons": noisy_moons,
            "blobs": blobs,
            "gaussian_quantiles": gaussian_quantiles,
            "no_structure":no_structure}

### START CODE HERE ### (choose your dataset)
dataset = "noisy_circles"
### END CODE HERE ###

X, Y = datasets[dataset]
X, Y = X.T, Y.reshape(1, Y.shape[0])

# make blobs binary
if dataset == "blobs":
    Y = Y%2

# Visualize the data
plt.scatter(X[0, :], X[1, :], c=Y, s=40, cmap=plt.cm.Spectral);    
plt.show()
            
### START CODE HERE ### (≈ 3 lines of code)
shape_X = X.shape
shape_Y = Y.shape
m = X.shape[1]  # training set size
### END CODE HERE ###

print ('The shape of X is: ' + str(shape_X))
print ('The shape of Y is: ' + str(shape_Y))
print ('I have m = %d training examples!' % (m))
# Train the logistic regression classifier
clf = sklearn.linear_model.LogisticRegressionCV();
clf.fit(X.T, Y.T);
# Plot the decision boundary for logistic regression
plot_decision_boundary(lambda x: clf.predict(x), X, Y)
plt.title("Logistic Regression")

# Print accuracy
LR_predictions = clf.predict(X.T)
print ('Accuracy of logistic regression: %d ' % float((np.dot(Y,LR_predictions) + np.dot(1-Y,1-LR_predictions))/float(Y.size)*100) +
       '% ' + "(percentage of correctly labelled datapoints)")

plt.show()
# Build a model with a n_h-dimensional hidden layer
parameters = nn_model(X, Y, n_h = 20, num_iterations = 10000, print_cost=True)
# Plot the decision boundary
plot_decision_boundary(lambda x: predict(parameters, x.T), X, Y)
plt.title("Decision Boundary for hidden layer size " + str(20))
# Print accuracy
predictions = predict(parameters, X)
print ('Accuracy: %d' % float((np.dot(Y,predictions.T) + np.dot(1-Y,1-predictions.T))/float(Y.size)*100) + '%')

