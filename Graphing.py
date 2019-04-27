#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:25:13 2019

@author: Jonathan S. Kent
"""

import matplotlib.pyplot as plt
import numpy as np

import Settings
import StockData

# Graphs the percent changes of stock price multipliers over a day
def stock_multiplier_graph(multipliers):
    for i in multipliers:
        plt.plot(i)
    axes = plt.gca()
    axes.set_xlim([-5, Settings.minutes + 5])
    plt.xticks(30 * np.arange(14), Settings.xlabels, rotation = Settings.rot)
    plt.figure()
    