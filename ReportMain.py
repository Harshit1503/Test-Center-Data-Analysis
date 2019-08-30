# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 00:33:06 2019

@author: Harshit
"""
import sys
from db_QUERY_Years_List import dbQUERY_Years_List
from R0001_Student_Distribution_PieChart_Report import dbQUERY_StudentDistributionPieChart
from R0002_Course_Distribution_PieChart_Report import dbQUERY_CourseDistributionPieChart
from R0003_Student_Distribution_BarPlot_Report import dbQUERY_StudentDistributionBarPlot
from R0004_Exams_By_Weekday_BarPlot_Report import dbQUERY_ExamsByWeekday
from R0005_Exams_By_Month_Barplot_Report import dbQUERY_ExamsByMonth
#
from R0001_Student_Distribution_PieChart_Report import StudentDistributionPieChart
from R0002_Course_Distribution_PieChart_Report import CourseDistributionPieChart
from R0003_Student_Distribution_BarPlot_Report import StudentDistributionBarPlot
from R0004_Exams_By_Weekday_BarPlot_Report import ExamsByWeekday
from R0005_Exams_By_Month_Barplot_Report import ExamsByMonth


def main():
    
    #Finding Years from Reporting Table of CWReporting Database:   
    yearsList = dbQUERY_Years_List.years_list()

        
    #Student Distribution across all three Sites        
    if (len(sys.argv) == 3 and sys.argv[2] == '1' and (sys.argv[1] in str(yearsList) or sys.argv[1] in ['all', 'All', 'ALL'])):
        
        aahCNT = cbbCNT = garCNT = 0
        yearVal = sys.argv[1]
        siteCountList = dbQUERY_StudentDistributionPieChart.student_distribution_pie_query(yearVal)

        aahCNT = siteCountList[0]
        cbbCNT = siteCountList[1]
        garCNT = siteCountList[2]

        StudentDistributionPieChart.student_distribution_pie(aahCNT, cbbCNT, garCNT, yearVal)           
        
    #Student Distribution across the Course    
    elif (len(sys.argv) == 3 and sys.argv[2] == '2' and (sys.argv[1] in str(yearsList) or sys.argv[1] in ['all', 'All', 'ALL'])):

        yearVal = sys.argv[1]
        courseWareCNT = blackBoardCNT = 0
            
        courseCountList = dbQUERY_CourseDistributionPieChart.course_distribution_pie_query(yearVal)
        
        courseWareCNT = courseCountList[0]
        blackBoardCNT = courseCountList[1]
        
        CourseDistributionPieChart.course_distribution_pie(courseWareCNT, blackBoardCNT, yearVal)

            
    #Student Distribution across the Sites for last 3 years
    elif (len(sys.argv) == 2 and sys.argv[1] == '3' and len(yearsList) >= 3):

        aahCNT = cbbCNT = garCNT = 0
        aahList = []
        cbbList = []
        garList = []
        aahParntList = []
        cbbParntList = []
        garParntList = []
        last_three_years_index = 3

        for yearIndx in range(len(yearsList[:last_three_years_index])):
            
            siteCountList = dbQUERY_StudentDistributionBarPlot.student_distribution_bar_plot_query(yearsList[yearIndx])
            aahCNT = siteCountList[0]
            cbbCNT = siteCountList[1]
            garCNT = siteCountList[2]   

            aahList.append(yearsList[yearIndx])
            aahList.append('AAH')
            aahList.append(aahCNT)
            cbbList.append(yearsList[yearIndx])
            cbbList.append('CBB')
            cbbList.append(cbbCNT)
            garList.append(yearsList[yearIndx])
            garList.append('GAR')
            garList.append(garCNT)
            
            aahTmpList = aahList[:]
            cbbTmpList = cbbList[:]
            garTmpList = garList[:]
            
            aahParntList.append(aahTmpList)
            cbbParntList.append(cbbTmpList)
            garParntList.append(garTmpList)

            del aahList[:]
            del cbbList[:]
            del garList[:]

    
        StudentDistributionBarPlot.student_distribution_bar_plot(aahParntList, cbbParntList, garParntList, yearsList)

    #Exams By Weekday           
    elif(len(sys.argv) == 3 and sys.argv[2] == '4' and (sys.argv[1] in str(yearsList) or sys.argv[1] in ['all', 'All', 'ALL'])):
        
        yearVal = sys.argv[1]
        weekDay_CNT = dbQUERY_ExamsByWeekday.exams_by_weekday_query(yearVal)
        ExamsByWeekday.exams_by_weekday_bar_plot(weekDay_CNT, yearVal)

    #Exams By Month        
    elif(len(sys.argv) == 3 and sys.argv[2] == '5' and (sys.argv[1] in str(yearsList) or sys.argv[1] in ['all', 'All', 'ALL'])):
        
        yearVal = sys.argv[1]
        month_CNT = dbQUERY_ExamsByMonth.exams_by_month_query(yearVal) 
        ExamsByMonth.exams_by_month_bar_plot(month_CNT, yearVal)
        
        
                    
    else:
        print("Incorrect arguments passed!")

       
if __name__ == "__main__":
    main()


 