#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:20:31 2020

@author: alina

I got the idea for this from kaggle's Lego dataset.
I am using the updated files from Rebrickable (I started on Nov 15, 2020)
and since the colors.csv file was "empty", I am using the one from kaggle
(it shouldn't really affect the outcome of my analysis). 

Resources:
https://www.kaggle.com/rtatman/lego-database
https://rebrickable.com/downloads/

For a later version of this project, I should create an API to keep
this up-to-date (https://rebrickable.com/api/).
"""


import pandas as pd
import numpy as np

# create the DataFrames with all the raw data
sets = pd.read_csv('sets.csv')
themes = pd.read_csv('themes.csv')
parts = pd.read_csv('parts.csv')
minifigs = pd.read_csv('minifigs.csv')
colors = pd.read_csv('colors.csv')

# start analyzing minifigs
minifigs['Harry Potter' in minifigs['name']] # KeyError: False

minifigs.loc['name' == 'Will.i.am'] # ???

minifigs['name'] == 'Will.i.am'

sets.columns
sets.columns
Out[51]: Index(['set_num', 'name', 'year', 'theme_id', 'num_parts'], dtype='object')

minifigs.columns
Out[52]: Index(['fig_num', 'name', 'num_parts'], dtype='object')

# if there is no relation between files, getting all the minifigures
# from each file will probe difficult


