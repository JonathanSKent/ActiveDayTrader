#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:19:10 2019

@author: jonathan
"""

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