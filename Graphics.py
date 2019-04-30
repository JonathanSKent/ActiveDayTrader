#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:06:33 2019

@author: Jonathan S. Kent
"""

import tkinter
from PIL import Image, ImageTk

import Settings
    
root = tkinter.Tk()    
root.geometry('1000x700')

load = Image.open(Settings.hold_loc)
render = ImageTk.PhotoImage(load)

img = tkinter.Label(image=render)
img.image = render
img.place(x=100, y=100)

tkinter.mainloop()