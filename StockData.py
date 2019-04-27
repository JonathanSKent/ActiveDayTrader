#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 19:11:02 2019

@author: Jonathan S. Kent
"""

from yahoo_fin import stock_info

import Settings

# Object that will fetch live stock price data
class data_fetch:
    def __init__(self, st = Settings.stock_ticks):
        self.stocks = st
        
    def get_data(self):
        return({tick : stock_info.get_live_price(tick) for tick in self.stocks})