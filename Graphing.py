#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 22:25:13 2019

@author: Jonathan S. Kent
"""

import matplotlib.pyplot
import numpy as np

import Settings
import StockData

# Graphs the percent changes of stock price multipliers over a day
def stock_multiplier_graph(multipliers):
    for i in multipliers:
        matplotlib.pyplot.plot(i)
    matplotlib.pyplot.figure()
    