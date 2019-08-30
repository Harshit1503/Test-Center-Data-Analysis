# -*- coding: utf-8 -*-
"""
Created on Mon May 13 01:51:08 2019

@author: Harshit
"""

import os
import pyodbc
from db_Connection import dbConnection



def student_distribution_pie_query(yearVal):

    #DB connection 
    connString = dbConnection.database_connection()
    conn = pyodbc.connect(connString)
    cursor = conn.cursor()
    
    #Absolute path of report directory
    abs_path = os.path.abspath(os.path.dirname(__file__))
    rel_path = "QUERY_StudentDistributionPieChart.txt"
    path = os.path.join(abs_path, rel_path)
    f = open(path, "r")
    
    #Query Index is assigned based on line number of query from QUERY_StudentDistributionPieChart.txt file:
    aah_query_index = 8
    cbb_query_index = 12
    gar_query_index = 16
    
    aah_allYear_query_index = 20
    cbb_allYear_query_index = 24
    gar_allYear_query_index = 28
    
    dbQuery = f.readlines()

    aah_query = dbQuery[aah_query_index]
    cbb_query = dbQuery[cbb_query_index]
    gar_query = dbQuery[gar_query_index]
    
    aah_allYear_query = dbQuery[aah_allYear_query_index]
    cbb_allYear_query = dbQuery[cbb_allYear_query_index]
    gar_allYear_query = dbQuery[gar_allYear_query_index]
    
    f.close()
    
    aahCNT = cbbCNT = garCNT = 0
    
    if yearVal not in ['all', 'All', 'ALL']: 
        #Query for AAH:
        curAAH = cursor.execute(aah_query, (yearVal))
        for row in curAAH:
            aahCNT = row.cnt
        
        #Query for CBB:
        curCBB = cursor.execute(cbb_query, (yearVal))
        for row in curCBB:
            cbbCNT = row.cnt
        
        #Query for GAR:       
        curGAR = cursor.execute(gar_query, (yearVal))
        for row in curGAR:
            garCNT = row.cnt
    
    else:
        curAAH = cursor.execute(aah_allYear_query)
        for row in curAAH:
            aahCNT = row.cnt
        
        curCBB = cursor.execute(cbb_allYear_query)
        for row in curCBB:
            cbbCNT = row.cnt
       
        curGAR = cursor.execute(gar_allYear_query)
        for row in curGAR:
            garCNT = row.cnt        


    return [aahCNT, cbbCNT, garCNT]
        
