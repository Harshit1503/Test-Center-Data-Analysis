# -*- coding: utf-8 -*-
"""
Created on Wed May  8 00:40:39 2019

@author: Harshit
"""

import os

def database_connection():

    #Absolute path of report directory
    abs_path = os.path.abspath(os.path.dirname(__file__))
    rel_path = "dbConnectionString.txt"
    path = os.path.join(abs_path, rel_path)
    f = open(path, "r")
    dbConnString = f.readlines()
    f.close()
    
    return(dbConnString[0])