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

def run(force_new = False):
    if os.path.isfile(Settings.model_loc) and not force_new:
        model = Model.trade_model(load = True)
    else:
        model = Model.trade_model()
        
    data = StockData.data_obj()
    
    first_run = True
    holdings = np.array([1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
    fund_value = [1]
    
    time.sleep(90)
    
    while ((datetime.datetime.now().hour < 15) and 
        ((datetime.datetime.now().hour > 8) or 
         ((datetime.datetime.now().hour == 8) and 
          (datetime.datetime.now().minute >= 30)))):
        while datetime.datetime.now().second != 0:
            time.sleep(0.5)
        
        data.update()
        
        tm = data.tick_multiplier()
        
        if not first_run:
            model.train(tm)
            
        fund_value.append((holdings * np.array(tm.cpu())).sum() * fund_value[-1])
            
        holdings = model.forward(tm[:-1]).cpu().detach().numpy().reshape([-1])
        Graphing.current_holdings_graph(holdings)
        Graphing.stock_multiplier_graph(np.array(data.pct_hist.t().cpu()), fund_value)
        
        if datetime.datetime.now().minute == 59:
            model.save()
        
        first_run = False
        
run()