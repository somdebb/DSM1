# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:08:04 2021

@author: sombanerjee
"""

import pandas as pd
import numpy as np
import os

os.chdir(r"C:\Users\sombanerjee\Documents\power purchase MIS\WEEK 150321-210321\WEEK 150321-210321\JSEB")

df = pd.read_csv("15_21frequency.csv")
df = df.drop(columns = df.columns[0])
map_array = np.arange(49.5,50.5,0.01)
map_freq = np.arange(0,100,1)
my_map = dict(zip(map_freq,map_array))
freq_new = pd.DataFrame()
for x in df.columns:
    freq_new[x] = df[x].map(my_map)