# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 17:01:26 2018

@author: sivavg
"""

import numpy as np  
import matplotlib.pyplot as plt  
def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()
graph('1 + np.sin(2 * np.pi * x)', np.arange(0.0, 2.0, 0.01))

#1 + np.sin(2 * np.pi * t)
def heart():
    t = np.arange(0,2*np.pi, 0.1)
    x = 16*np.sin(t)**3
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    plt.plot(x,y)
    plt.show()
heart()

(x2+y2-1)3=x2y3