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
def stock_multiplier_graph(multipliers, fund_value):
    for i in range(len(multipliers)):
        plt.plot(multipliers[i], label = Settings.stock_ticks[i].upper(), linestyle = '--')
    plt.plot(fund_value, label = 'Fund')
    plt.xlabel("Time (EST)", fontsize = 'x-large')
    plt.ylabel("Value Relative to Day Start", fontsize = 'x-large')
    plt.title("Value of Assets Relative to Day Start", fontsize = 'xx-large')
    axes = plt.gca()
    axes.set_xlim([-5, Settings.minutes + 5])
    plt.xticks(30 * np.arange(14), Settings.xlabels, rotation = -60)
    plt.legend(loc='upper right')
    plt.figure()
    