#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 12:51:17 2019

@author: Jonathan S. Kent
"""

import os
import datetime
import time
import numpy as np

import Settings
import StockData
import Model
import Graphing

def run():
    if os.path.isfile(Settings.model_loc):
        model = Model.trade_model(load = True)
    else:
        model = Model.trade_model()
        
    data = StockData.data_obj()
    
    first_run = True
    holdings = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    fund_value = [1]
    
    while ((datetime.datetime.now().hour < 16) and 
        ((datetime.datetime.now().hour > 9) or 
         ((datetime.datetime.now().hour == 9) and 
          (datetime.datetime.now().minute >= 30)))):
        while datetime.datetime.now().second != 0:
            time.sleep(0.5)
        
        data.update()
        if not first_run:
            model.train(data.tick_multiplier())
            
        fund_value.append((holdings * np.array(data.tick_multiplier().cpu())).sum() * fund_value[-1])
            
        holdings = model.forward(data.curr_pct).cpu().detach().numpy().reshape([-1])
        print(holdings)
        Graphing.current_holdings_graph(holdings)
        Graphing.stock_multiplier_graph(np.array(data.pct_hist.t().cpu()), fund_value)
        
        if datetime.datetime.now().minute == 59:
            model.save()
        
        first_run = False