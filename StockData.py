#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:11:02 2019

@author: Jonathan S. Kent
"""

from yahoo_fin import stock_info
import torch
import numpy as np
import joblib

import Settings

# Object that will fetch live stock price data
class data_obj:
    def __init__(self, st = Settings.stock_ticks):
        print("Initializing data object...")
        self.stocks = st
        self.curr_price = get_data(self.stocks)
        self.basis = torch.tensor(self.curr_price).to(Settings.device)
        self.pct_hist = torch.ones(1, len(self.stocks))
        self.curr_pct = self.pct_hist[0].to(Settings.device)
        self.old_pct = self.pct_hist[0].to(Settings.device)
        print("Data object initialized. Price basis: ", list(np.array(self.basis.cpu())))
        Settings.d1()
        
    def update(self):
        print("Updating stock price information...")
        self.old_pct = self.curr_pct
        self.curr_price = get_data(self.stocks)
        self.curr_pct = torch.tensor(self.curr_price).to(Settings.device) / self.basis
        self.pct_hist = torch.cat((self.pct_hist, self.curr_pct.reshape([1, -1]).cpu()))
        print("Stock price information updated.")
        Settings.d2()
        
    def tick_multiplier(self):
        return(torch.cat((self.curr_pct / self.old_pct, torch.tensor([1], dtype = torch.float32).to(Settings.device))))
        
def get_data(stocks):
    return([stock_info.get_live_price(tick) for tick in stocks])