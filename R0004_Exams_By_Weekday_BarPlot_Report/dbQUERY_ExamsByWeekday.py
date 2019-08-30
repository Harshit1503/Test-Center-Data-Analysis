# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 02:25:35 2019

@author: Harshit
"""

import os
import pyodbc
from db_Connection import dbConnection


def exams_by_weekday_query(yearVal):

    #DB connection 
    connString = dbConnection.database_connection()
    conn = pyodbc.connect(connString)
    cursor = conn.cursor()
    
    #Absolute path of report directory
    abs_path = os.path.abspath(os.path.dirname(__file__))
    rel_path = "QUERY_ExamsByWeekday.txt"
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

    weekday_List = [1, 2, 3, 4, 5, 6, 7]
    weekday_Index_Key = 2
    weekday_Index_Count = 3
    aah_Weekday_CNT_Dict = dict.fromkeys(weekday_List, 0)
    cbb_Weekday_CNT_Dict = dict.fromkeys(weekday_List, 0)
    gar_Weekday_CNT_Dict = dict.fromkeys(weekday_List, 0)
    
    if yearVal not in ['all', 'All', 'ALL']:
    
        #Query for AAH:
        curAAH = cursor.execute(aah_query, (yearVal))
        for row in curAAH:
#            print(row[3])
            if row[weekday_Index_Key] in aah_Weekday_CNT_Dict:
                aah_Weekday_CNT_Dict[row[weekday_Index_Key]] = row[weekday_Index_Count]
        
        
        #Query for CBB:
        curCBB = cursor.execute(cbb_query, (yearVal))
        for row in curCBB:
            if row[weekday_Index_Key] in cbb_Weekday_CNT_Dict:
                cbb_Weekday_CNT_Dict[row[weekday_Index_Key]] = row[weekday_Index_Count]

        
        #Query for GAR:    
        curGAR = cursor.execute(gar_query, (yearVal))
        for row in curGAR:
            if row[weekday_Index_Key] in gar_Weekday_CNT_Dict:
                gar_Weekday_CNT_Dict[row[weekday_Index_Key]] = row[weekday_Index_Count]

            
    else:
        #Query for AAH:
        curAAH = cursor.execute(aah_allYear_query)
        for row in curAAH:
            if row[weekday_Index_Key] in aah_Weekday_CNT_Dict:
                aah_Weekday_CNT_Dict[row[weekday_Index_Key]] = row[weekday_Index_Count]

    
        #Query for CBB:
        curCBB = cursor.execute(cbb_allYear_query)
        for row in curCBB:
            if row[weekday_Index_Key] in cbb_Weekday_CNT_Dict:
                cbb_Weekday_CNT_Dict[row[weekday_Index_Key]] = row[weekday_Index_Count]

            
        #Query for GAR:    
        curGAR = cursor.execute(gar_allYear_query)
        for row in curGAR:
            if row[weekday_Index_Key] in gar_Weekday_CNT_Dict:
                gar_Weekday_CNT_Dict[row[weekday_Index_Key]] = row[weekday_Index_Count]

    
    return aah_Weekday_CNT_Dict, cbb_Weekday_CNT_Dict, gar_Weekday_CNT_Dict

        