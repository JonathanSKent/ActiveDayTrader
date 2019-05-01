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
        plt.plot(multipliers[i], label = Settings.stock_ticks[i].upper(), linestyle = '--', alpha = 0.55)
    plt.plot(fund_value, label = 'Fund')
    plt.xlabel("Time (EST)", fontsize = 'x-large')
    plt.ylabel("Value Relative to Day Start", fontsize = 'x-large')
    plt.title("Value of Assets Relative to Day Start", fontsize = 'xx-large')
    axes = plt.gca()
    axes.set_xlim([-5, Settings.minutes + 5])
    plt.xticks(30 * np.arange(14), Settings.xlabels, rotation = -25, fontsize = 'x-small')
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(Settings.ass_loc)
    plt.clf()
    
# Produces a bar chart of relative stock holdings at a given time
def current_holdings_graph(holdings):
    plt.bar(range(len(holdings)), holdings)
    plt.xticks(range(len(holdings)), [i.upper() for i in Settings.stock_ticks] + ['$'])
    plt.xlabel("Assets", fontsize = 'x-large')
    plt.ylabel("Relative Holdings", fontsize = 'x-large')
    plt.title("Currently Held Position", fontsize = 'xx-large')
    axes = plt.gca()
    axes.set_ylim([0, 1])
    plt.tight_layout()
    plt.savefig(Settings.hold_loc)
    plt.clf()