# -*- coding: utf-8 -*-
"""
Created on Sat May  4 18:53:55 2019

@author: Harshit
"""

import os
import pyodbc
from db_Connection import dbConnection



def years_list():

    #DB connection 
    connString = dbConnection.database_connection()
    conn = pyodbc.connect(connString)
    cursor = conn.cursor()
    
    #Absolute path of report directory
    abs_path = os.path.abspath(os.path.dirname(__file__))   
    rel_path = "QUERY_YearsList.txt"
    path = os.path.join(abs_path, rel_path)
    f = open(path, "r")
    
    #Query Index is assigned based on line number of query from QUERY_YearsList.txt file:
    yearsList_query_index = 8
    dbQuery = f.readlines()
    yearsList_query = dbQuery[yearsList_query_index]
    f.close()
    
    curYEARS = cursor.execute(yearsList_query)
    yearsList = []
    for row in curYEARS:
        yearsList.append(row.YEARS)
    
    return (yearsList)

