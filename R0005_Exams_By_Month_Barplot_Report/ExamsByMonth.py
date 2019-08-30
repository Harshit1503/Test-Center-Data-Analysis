# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 21:19:50 2019

@author: Harshit
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from datetime import date


def exams_by_month_bar_plot(month_CNT_Tuple, yearVal):
    
    # set width of bar
    barWidth = 0.25
    
    plt.rc('figure', figsize=(27, 15))
    font = {'weight' : 'bold',
                'size'   : 22}
        
    plt.rc('font', **font)
    
    # set height of bar
    aah = [month_CNT_Tuple[0][1], month_CNT_Tuple[0][2], month_CNT_Tuple[0][3], month_CNT_Tuple[0][4], month_CNT_Tuple[0][5], month_CNT_Tuple[0][6], month_CNT_Tuple[0][7], month_CNT_Tuple[0][8], month_CNT_Tuple[0][9], month_CNT_Tuple[0][10], month_CNT_Tuple[0][11], month_CNT_Tuple[0][12]]
    cbb = [month_CNT_Tuple[1][1], month_CNT_Tuple[1][2], month_CNT_Tuple[1][3], month_CNT_Tuple[1][4], month_CNT_Tuple[1][5], month_CNT_Tuple[1][6], month_CNT_Tuple[1][7], month_CNT_Tuple[1][8], month_CNT_Tuple[1][9], month_CNT_Tuple[1][10], month_CNT_Tuple[1][11], month_CNT_Tuple[1][12]]
    gar = [month_CNT_Tuple[2][1], month_CNT_Tuple[2][2], month_CNT_Tuple[2][3], month_CNT_Tuple[2][4], month_CNT_Tuple[2][5], month_CNT_Tuple[2][6], month_CNT_Tuple[2][7], month_CNT_Tuple[2][8], month_CNT_Tuple[2][9], month_CNT_Tuple[2][10], month_CNT_Tuple[2][11], month_CNT_Tuple[2][12]]
     
    # Set position of bar on X axis
    r1 = np.arange(len(aah))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
     
    # Make the plot
    plt.bar(r1, aah, color='steelblue', width=barWidth, edgecolor='white', label='AAH')
    plt.bar(r2, cbb, color='darkorange', width=barWidth, edgecolor='white', label='CBB')
    plt.bar(r3, gar, color='c', width=barWidth, edgecolor='white', label='GAR')
     
    # Add xticks on the middle of the group bars
    plt.xlabel("\n"+'Month', fontsize = 25, fontweight='bold')
    plt.ylabel('Number of Students', fontsize = 25, weight = "bold")
    if yearVal not in ['all', 'All', 'ALL']:
        plt.title("Exams By Month: "+str(yearVal)+"\n", fontsize = 30, weight="bold") 
    else:
        plt.title('Exams By Month'+"\n", fontsize = 30, weight = "bold")
        
    plt.xticks([r + barWidth for r in range(len(aah))], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
     
    # Create legend & Show graphic
    plt.legend(['AAH', 'CBB', 'GAR'])
    
    #Save the Pie Chart image to respective report directory   
    #Absolute path of report directory
    abs_path = os.path.abspath(os.path.dirname(__file__))
    rel_path = "output"    
    path = os.path.join(abs_path, rel_path)
    
    if not os.path.exists(path):
        print("Image Folder Created!")
        os.makedirs(path)

    if yearVal not in ['all', 'All', 'ALL']:
        file_name = 'Exams_By_Month_BarPlot_' + str(yearVal) +'.png'
    else:
        file_name = 'Exams_By_Month_BarPlot_all.png'
    
    my_dpi = 72
#    plt.figure(figsize=(1944/my_dpi, 1080/my_dpi), dpi=my_dpi)
#    plt.savefig('my_fig.png', dpi=my_dpi)
    plt.savefig(os.path.join(path, file_name), dpi = my_dpi)
    
    plt.show()

    image_path_input = path
    image_path_output = path
    fnt = ImageFont.truetype("arial.ttf", 25)
    image_name_input = '\\' + file_name
    today = date.today()
    im = Image.open(image_path_input + image_name_input)
    position = (1790, 1030)
    message = today.strftime("%m/%d/%Y")
    
    # initialise the drawing context with the image object as background
    draw = ImageDraw.Draw(im)
    draw.text(position, message, font = fnt, fill = "black")
    
    im.show()
    image_name_output = '\\' + file_name
    im.save(image_path_output + image_name_output)
    
