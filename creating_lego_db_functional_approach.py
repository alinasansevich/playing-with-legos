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

conn = sqlite3.connect('lego_func_appr.db')
cur = conn.cursor()

try:
    cur.executescript("""
                      DROP TABLE IF EXISTS Sets
                      DROP TABLE IF EXISTS Themes
                      DROP TABLE IF EXISTS Parts
                      DROP TABLE IF EXISTS Part_Categories
                      DROP TABLE IF EXISTS Colors
                      DROP TABLE IF EXISTS Inventories
                      DROP TABLE IF EXISTS Inventory_Parts
                      DROP TABLE IF EXISTS Inventory_Sets
                      
                      CREATE TABLE Sets(
                          Set_Num TEXT NOT NULL,
                          Name TEXT,
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

### create top-level function load_data
def load_data(db_name, enzymesXXX, referencesXXX): # CHANGE PARAMETERS!
    """  """
    try:
        load_sets_data()
        load_themes_data()
        load_parts_data()
        load_part_categories_data()
        load_colors_data()
        load_inventories_data()
        load_inventory_parts_data()
        load_inventory_sets_data()
        conn.commit()
    except sqlite3.OperationalError as ex:
        print(ex, file=sys.stderr)
        raise
                    
### CREATE A SEPARATE FUNCTION FOR EACH TABLE!
def load_sets_data():
    pass

def load_themes_data():
    pass

def load_parts_data():
    pass

def load_part_categories_data():
    pass

def load_colors_data():
    pass

def load_inventories_data():
    pass

def load_inventory_parts_data():
    pass

def load_inventory_sets_data():
    pass
                      
