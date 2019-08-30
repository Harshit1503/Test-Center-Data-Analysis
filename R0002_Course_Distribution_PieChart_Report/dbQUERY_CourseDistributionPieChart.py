# -*- coding: utf-8 -*-
"""
Created on Mon May 13 01:58:47 2019

@author: Harshit
"""

import os
import pyodbc
from db_Connection import dbConnection



def course_distribution_pie_query(yearVal):

    #DB connection 
    connString = dbConnection.database_connection()
    conn = pyodbc.connect(connString)
    cursor = conn.cursor()
    
    #Absolute path of report directory
    abs_path = os.path.abspath(os.path.dirname(__file__))   
    rel_path = "QUERY_CourseDistributionPieChart.txt"
    path = os.path.join(abs_path, rel_path)
    f = open(path, "r")
    
    #Query Index is assigned based on line number of query from QUERY_CourseDistributionPieChart.txt file:
    courseWare_query_index = 8
    blackboard_query_index = 12
    
    courseWare_allYear_query_index = 16
    blackboard_allYear_query_index = 20

    dbQuery = f.readlines()

    courseWare_query = dbQuery[courseWare_query_index]
    blackboard_query = dbQuery[blackboard_query_index]
    
    courseWare_allYear_query = dbQuery[courseWare_allYear_query_index]
    blackboard_allYear_query = dbQuery[blackboard_allYear_query_index]

    f.close()
    
    courseWareCNT = blackBoardCNT = 0
    
    if yearVal not in ['all', 'All', 'ALL']:
        curCourseWare = cursor.execute(courseWare_query, (yearVal))
        for row in curCourseWare:
            courseWareCNT = row.cnt
        
        curBlackBoard = cursor.execute(blackboard_query, (yearVal))
        for row in curBlackBoard:
            blackBoardCNT = row.cnt
            
    else:
        curCourseWare = cursor.execute(courseWare_allYear_query)
        for row in curCourseWare:
            courseWareCNT = row.cnt
        
        curBlackBoard = cursor.execute(blackboard_allYear_query)
        for row in curBlackBoard:
            blackBoardCNT = row.cnt
    
        
    return [courseWareCNT, blackBoardCNT]

