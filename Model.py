#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 20:49:31 2019

@author: Jonathan S. Kent
"""

import torch
import joblib

import Settings

class trade_model():
    def __init__(self, load = False, loc = Settings.model_loc):
        if load:
            self.model1, self.lstm, self.model2 = joblib.load(loc)
            
        else:
            self.model1 = torch.nn.Sequential(torch.nn.Linear(5, 50),
                                          torch.nn.ReLU()).to(Settings.device)
            self.lstm = torch.nn.LSTM(50, 50, 2).to(Settings.device)
            self.model2 = torch.nn.Sequential(torch.nn.Linear(50, 50),
                                          torch.nn.ReLU(),
                                          torch.nn.Linear(50, 6),
                                          torch.nn.Softmax(dim = -1)).to(Settings.device)
        self.hidden = False
        self.optimizer = torch.optim.Adam(list(self.model1.parameters()) +
                                          list(self.lstm.parameters()) +
                                          list(self.model2.parameters()),
                                          lr = 0.01)
        
    def forward(self, inp):
        inp_ = self.model1(inp.to(Settings.device))
        if self.hidden:
            inp_, self.hidden = self.lstm(inp_.view(1, 1, -1), self.hidden)
        else:
            inp_, self.hidden = self.lstm(inp_.view(1, 1, -1))
        self.out = self.model2(inp_)
        return(self.out.reshape(1, -1))
        
    def train(self, mult):
        self.optimizer.zero_grad()
        loss = -(self.out * mult.to(Settings.device)).sum()
        loss.backward(retain_graph=True)
        self.optimizer.step()
        
    def save(self, loc = Settings.model_loc):
        joblib.dump([self.model1, self.lstm, self.model2], loc)