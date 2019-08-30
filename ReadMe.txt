##################ReadMe#################
The following project shows the Test Center Data Analysis done using Python and SQLServer.

Following driver and libraries are required to run the Python Programmes:
1) Install Microsoft® ODBC Driver 17 for SQL Server® - Windows, Linux, & macOS.
2) run pip install -r Requirements.txt

Instructions to run the python code on windows command prompt:
1) Run the ReportMain.py which takes different parameters for different reports.
To call StudentDistributionPieChart.py program from ReportMain.py pass 2nd argument as 1 and 1st argument as Year or all/All/ALL.
For example:
C:\Users\harshit\Desktop\CASA>python ReportMain.py 2018 1
C:\Users\harshit\Desktop\CASA>python ReportMain.py All 1

2) Run the ReportMain.py and to call CourseDistributionPieChart.py pass 2nd argument as 2 and 1st argument as Year or all/All/ALL.
For example:
C:\Users\harshit\Desktop\CASA>python ReportMain.py 2018 2
C:\Users\harshit\Desktop\CASA>python ReportMain.py all 2

3) Run the ReportMain.py and to call StudentDistributionBarPlot.py pass only one argument as 3.
For example:
C:\Users\harshit\Desktop\CASA>python ReportMain.py 3

Report 4 and 5 can be run the same way as 1 and 2 are running.