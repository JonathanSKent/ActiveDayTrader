#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:19:10 2019

@author: Jonathan S. Kent
"""

import os
import torch

# Prints these to demarcate between actions
demarc_long = "~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~#~"
def d1():
    print(demarc_long)
    
demarc_short = "~#~#~#~#~#~"
def d2():
    print(demarc_short)

# Whether or not a gpu is available
device = ['cpu', 'cuda'][torch.cuda.is_available()]

# Tickers of the stocks being traded
stock_ticks = ['f', 'goog', 'cost', 'hon', 'amd']

# Minutes in a trading day, from 9:30 AM EST to 4:00 PM EST
minutes = 390

# X-axis tick labels on the multiplier graph
xlabels = ['9:30 AM', '10:00 AM', '10:30 AM', '11:00 AM', 
          '11:30 AM', '12:00 PM', '12:30 PM', '1:00 PM', 
          '1:30 PM', '2:00 PM', '2:30 PM', '3:90 PM', 
          '3:30 PM', '4:00 PM']

# Directory where the latest graphs get saved
hold_loc = os.path.join(os.getcwd(), 'holdings.png')
ass_loc = os.path.join(os.getcwd(), 'assets.png')

# Directory where the model is saved
model_loc = os.path.join(os.getcwd(), 'model.nn')