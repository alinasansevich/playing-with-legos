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
import matplotlib.pyplot as plt

# create the DataFrames with all the raw data
sets = pd.read_csv('sets.csv')
themes = pd.read_csv('themes.csv')
parts = pd.read_csv('parts.csv')
minifigs = pd.read_csv('minifigs.csv')
colors = pd.read_csv('colors.csv')

inventories = pd.read_csv('inventories.csv')
inv_parts = pd.read_csv('inventory_parts.csv')
inv_sets = pd.read_csv('inventory_sets.csv')



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
# from each file will be difficult  >> regex?

serie = parts['part_material'] != 'Plastic'
parts[serie]


inventories.columns
Out[30]: Index(['id', 'version', 'set_num'], dtype='object')

inv_sets.columns
Out[31]: Index(['inventory_id', 'set_num', 'quantity'], dtype='object')

inv_parts.columns
Out[32]: Index(['inventory_id', 'part_num', 'color_id', 'quantity', 'is_spare'], dtype='object')



######
# how many different lego bricks
## which one is the most frequent? which one is the least frequent? in which set?

# how many different colors
## which one is the most frequent? which one is the least frequent? in which set?
colors.head()

colors.columns
len(colors) # 135 rows
unique_names = colors.name.unique() # type: np.ndarray
unique_names.size # 135 color names

unique_rgb = colors.rgb.unique() # type: np.ndarray
unique_rgb.size # 124 rgb codes

trans = colors[colors['is_trans'] == 't'] # sub_df with only trans parts
trans.size # 112 transparent parts

# how many with "Glitter"?
trans['name'].str.contains('Glitter').size # 28

glit = trans['name'].str.contains('Glitter') # Series w/ bool values
glit.values.sum() # 5  >>> there are 5 transparent parts with glitter


glitter = trans[trans['name'].str.contains('Glitter')]
glitter.size # 20 ????? 8 missing????
num_of_glitter = glitter['is_trans'].values.sum() # 'ttttt' XD

x = colors[colors['name'].str.contains('Glitter')]
x['is_trans'].values.sum() # 'ttttt' >>> only transparent parts have glitter


##### extract each color and plot histogram

# create a dictionary with common colors
color_names = ['Blue', 'Green', 'Red', 'Yellow', 'Orange', 'Purple', 'Pink', 'White', 'Black', 'Brown', 'Clear', 'Gray', 'Gold', 'Silver', 'Copper', 'Violet'] 
colors_dict = {}
colors_totals = {}

for color in color_names:
    df = colors[colors['name'].str.contains(color)]
    colors_dict[color] = df
    colors_totals[color] = len(df)

len(unique_rgb) # 124
len(unique_names) # 135
sum(colors_totals.values()) # 118
# 17 colors missing

# find all unusual colors
colors["unusual_colors"] = colors['name'].apply(lambda x: 0 if any(i in x for i in color_names) else 1)

unusual_colors = colors[colors['unusual_colors'] == 1]
len(unusual_colors) # 26
  

unique_rgb = colors.rgb.unique() # type: np.ndarray
unique_rgb.size # 124 rgb codes

colors_rgb = colors['rgb'] # pd.Series
len(colors_rgb) # 135
# find all rgb values that are duplicated, keep all values:
dup_bool = colors_rgb.duplicated(keep=False)
rgb_dups = colors['rgb'][dup_bool.values]

len(rgb_dups) # 20

dup_names = colors['name'][dup_bool]

dup_colors = dup_names.to_frame().join(rgb_dups)
sorted_dups = dup_colors.sort_values(by=['rgb'])


# how many "Glow"?
glow = colors[colors['name'].str.contains('Glow')]
len(glow) # 3 only 3 parts are Glow in the Dark



# how many themes? 


# how many Harry, Hermione and Ron?

# distribution
# frequency
# correlation?

#### what variables do I have?




# set + themes >>> puedo ver a que theme pertenece cada set

# is transp, numero de piezas de cada color, numero de colores

#inventory_parts une varios archivos

# parts >>> different materials