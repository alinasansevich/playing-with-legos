#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:21:26 2021

@author: alina

I got the idea for this from kaggle's Lego dataset.
I am using the updated files from Rebrickable (I started on Nov 15, 2020)
and since the colors.csv file was "empty", I am using the one from kaggle
(it shouldn't really affect the outcome of my analysis). 

Resources:
https://www.kaggle.com/rtatman/lego-database
https://rebrickable.com/downloads/

Here all I want to do is to create the database following a functional approach,
inspired by the code from the book "Bioinformatics Programming Using Python"
"""

import sqlite3
import sys
import csv


file_names = ['sets.csv',
              'themes.csv',
              'parts.csv',
              'part_categories.csv',
              'colors.csv',
              'inventories.csv',
              'inventory_parts.csv',
              'inventory_sets.csv']

table_names = ['Sets',
               'Themes', 
               'Parts', 
               'Part_Categories',
               'Colors', 
               'Inventories',
               'Inventory_Parts',
               'Inventory_Sets']

def read_headers(file_names, table_names):
    """
    Extracts the number of columns from each file's header,
    creates an INSERT query string with the corresponding table name and 
    number of values to insert and appends to a queries list.
    Returns the list with all the queries.
    """
    # open .csv and find number of columns
    
    queries = []
    for file in file_names:
        with open(file) as f:
            header = f.readline()
            header = header[:-1] # drop '\n'
            num_columns = len(header.split(','))
            
            values = '?, ' * num_columns
            values = values[:-2]
            
            query = "INSERT INTO {} VALUES ({})".format(
                table_names[file_names.index(file)], values)
            queries.append(query)
    
    return queries

def read_csv_n_load_data(csv_file, query):
    """
    Read .csv file row by row and insert values into table.
    """
    # open .csv and find number of columns
    with open(csv_file) as f:
        header = f.readline() # read header just to skip it
        for line in f:
            row = line[:-1]
            row = tuple(row.split(','))
            values = tuple([row[i] for i in range(len(row))])            
            cur.execute(query, values)

def load_data(file_names, queries):
    """
    Loads data in the database's tables.
    """
    try:
        for file in file_names:
            read_csv_n_load_data(file, queries[file_names.index(file)])
        conn.commit()
    except sqlite3.OperationalError as ex:
        print(ex, file=sys.stderr)
        raise

conn = sqlite3.connect('lego_func_appr.db')
cur = conn.cursor()

# create tables
try:
    cur.executescript("""                      
                      CREATE TABLE Sets(
                          Set_Num TEXT NOT NULL,
                          Name TEXT,
                          Year INTEGER, 
                          Theme_Id INTEGER,
                          Num_Parts INTEGER
                          );
                      
                      CREATE TABLE Themes(
                          Id INTEGER NOT NULL,
                          Name TEXT,
                          Parent_Id INTEGER                          
                          );
                      
                      CREATE TABLE Parts(
                          Part_Num TEXT NOT NULL,
                          Name TEXT,
                          Part_Cat_Id INTEGER,
                          Part_Material TEXT
                          );
                      
                      CREATE TABLE Part_Categories(
                          Id INTEGER NOT NULL,
                          Name TEXT
                          );
                      
                      CREATE TABLE Colors(
                          Id INTEGER NOT NULL,
                          Name TEXT,
                          RGB TEXT,
                          Is_Trans TEXT                          
                          );
                      
                      CREATE TABLE Inventories(
                          Id INTEGER NOT NULL,
                          Version INTEGER,
                          Set_Num TEXT
                          );
                      
                      CREATE TABLE Inventory_Parts(
                          Inventory_Id INTEGER NOT NULL,
                          Part_Num TEXT,
                          Color_Id INTEGER,
                          Quantity INTEGER,
                          Is_Spare TEXT
                          );
                      
                      CREATE TABLE Inventory_Sets(
                          Inventory_Id INTEGER NOT NULL,
                          Set_Num TEXT,
                          Quantity INTEGER
                          );
                      """)
                      
except sqlite3.OperationalError as err:
    print(err, file=sys.stderr)
    conn.rollback() # abort changes
    raise

conn.commit()

# ### Once all tables are created, I have 2 possible ways to insert data:
#     # using pandas:
#     sets = pd.read_csv('sets.csv')
#     sets.to_sql('Sets', conn, if_exists='append', index=False)
    
#     # or using the csv module and sqlite3 (INSERT INTO...)
#     I will use this second approach since I have already used
#     the pandas approach in the notebook analysis.

# create all queries
queries = read_headers(file_names, table_names)

# load data into db
load_data(file_names, queries)

        
    
# I'm here:
    # try using pd.read_csv + pd.to_csv(sep='Tab')






# query = 'INSERT INTO Sets VALUES (?, ?, ?, ?, ?)'

# with open('themes.csv') as f:
#     header = f.readline() # read header just to skip it
#     for line in f:
#         row = line[:-1]
#         row = tuple(row.split(','))
#         values = [row[i] for i in range(len(row))]          
#         cur.execute(query, values)







                       # DROP TABLE IF EXISTS Sets
                       # DROP TABLE IF EXISTS Themes
                       # DROP TABLE IF EXISTS Parts
                       # DROP TABLE IF EXISTS Part_Categories
                       # DROP TABLE IF EXISTS Colors
                       # DROP TABLE IF EXISTS Inventories
                       # DROP TABLE IF EXISTS Inventory_Parts
                       # DROP TABLE IF EXISTS Inventory_Sets


