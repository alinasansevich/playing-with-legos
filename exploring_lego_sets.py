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

######
# how many different lego bricks
## which one is the most frequent? which one is the least frequent? in which set?

##############################################
# COLORS
##############################################
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

##############################################
# THEMES
##############################################
themes.head()
len(themes) # 598 rows
# how many themes? 
unique_themes = themes['name'].unique()
len(unique_themes) # 424
unique_theme_id = themes['id'].unique()
len(unique_theme_id) # 598 == rows! some names are repeated?

dups = themes['name'].duplicated(keep=False)
themes_dups = themes['name'][dups.values] # 249

themes_dups = themes_dups.sort_values()


hp = themes[themes['name'].str.contains('Harry')]
len(hp) # 4, one has a NaN parent_id

######### CONTINUE HERE UNTIL I GET ALL THE UNIQUE THEMES ID + NAMES


# set + themes >>> puedo ver a que theme pertenece cada set
sets.head()


##############################################
# MINIFIGURES
##############################################
minifigs.columns
minifigs.head()


# how many Harry, Hermione and Ron?
harry = minifigs[minifigs['name'].str.contains('Harry')] # 51
hermione = minifigs[minifigs['name'].str.contains('Hermione')] # 21
ron = minifigs[minifigs['name'].str.contains('Ron')] # 30

dumbledore = minifigs[minifigs['name'].str.contains('Dumbledore')] # 8

weasleys = minifigs[minifigs['name'].str.contains('Weasley')]
arthur = minifigs[minifigs['name'].str.contains('Arthur')] # 2
molly = minifigs[minifigs['name'].str.contains('Molly')] # 3
george = minifigs[minifigs['name'].str.contains('George')] # 7
fred = minifigs[minifigs['name'].str.contains('Fred')] # 8
ginny = minifigs[minifigs['name'].str.contains('Ginny')] # 6

voldemort = minifigs[minifigs['name'].str.contains('Voldemort')] # 8
professor = minifigs[minifigs['name'].str.contains('Professor')] # 34, but not all are Harry Potter's
malfoy = minifigs[minifigs['name'].str.contains('Malfoy')] # 19

# who else? WHAT can I do with this?


# distribution
# frequency
# correlation?

##############################################
# SETS
##############################################
len(sets) # 15903


##############################################
# PARTS
##############################################
# chech materials part_material
len(parts) # 37064

parts['part_material'].unique().describe
# Out[19]: 
# array(['Cardboard/Paper', 'Plastic', 'Cloth', 'Rubber', 'Metal'],
#       dtype=object)

parts['part_material'].value_counts()
# Out[30]: 
# Plastic            35496
# Cardboard/Paper      850
# Cloth                562
# Rubber               144
# Metal                 12
# Name: part_material, dtype: int64

##### I'm trying to go from parts to themes
cloth_parts = parts[parts['part_material'] == 'Cloth']
cloth_parts.name
##### I will follow a cloth part:
cloth_parts.loc[946, 'part_material']
# 'Cloth'
##### it's a shower curtain 
cloth_parts.loc[946, 'name']
# Duplo Cloth Shower Curtain

##### part_num: '11835'
cloth_parts.loc[946, 'part_num']
# '11835'

##### I look for it in inv_parts:
inv_parts.loc[inv_parts['part_num'] == '11835']
#         inventory_id part_num  color_id  quantity is_spare
# 449506         13186    11835        15         1        f
##### now I have it's inventory_id: 13186
##### I look for it in sets:
inv_sets.loc[inv_sets['inventory_id'] == 13186] # IS NOT THERE!???
##### IS NOT THERE!???

##### I will try with a flag this time:
cloth_parts.name
# 37044   Flag 4 x 5 [Plain]
cloth_parts.loc[37044, 'name']
# 'Flag 4 x 5 [Plain]'
cloth_parts.loc[37044, 'part_num']
##### part_num: 'x95'
##### I look for it in inv_parts:
inv_parts.loc[inv_parts['part_num'] == 'x95'] # IS NOT THERE!???
##### IS NOT THERE!???

# OK, no more cloth parts...
metal_parts = parts[parts['part_material'] == 'Metal']
metal_parts.name
##### I'm looking for a screwdriver this time:
##### 6738  Screwdriver with Old LEGO Logo [Metal]
metal_parts.loc[6738, 'name']
# 'Screwdriver with Old LEGO Logo [Metal]'
metal_parts.loc[6738, 'part_num']
##### part_num: '299'
##### I look for it in inv_parts:
inv_parts.loc[inv_parts['part_num'] == '299']
#         inventory_id part_num  color_id  quantity is_spare
# 255479          7623      299      9999         1        t
# 345903         10286      299      9999         1        t
# 363239         10796      299      9999         1        t
# 481681         14182      299      9999         1        t
##### I look for it in inv_sets, for inventory_id: 7623:
inv_sets.loc[inv_sets['inventory_id'] == 14182]  # IS NOT THERE!???
##### IS NOT THERE!???





