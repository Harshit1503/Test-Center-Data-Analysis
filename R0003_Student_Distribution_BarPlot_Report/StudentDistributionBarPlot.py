# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 10:34:12 2019

@author: Harshit
PGM 3
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from datetime import date


def student_distribution_bar_plot(aahParntList, cbbParntList, garParntList, yearsList):
    #plt.figure(figsize=(40,40))
    #plt.rcParams["figure.figsize"] = (10,10)    
    plt.rc('figure', figsize=(18, 18))    
    font = {#'family' : 'normal',
            'weight' : 'bold',
            'size'   : 22}
    
    plt.rc('font', **font)
    
    df = pd.DataFrame([aahParntList[2], cbbParntList[2], garParntList[2],
                       aahParntList[1], cbbParntList[1], garParntList[1],
                       aahParntList[0], cbbParntList[0], garParntList[0]],
                       columns=['group','column','val'])
    
    df.pivot("column", "group", "val").plot(kind='bar')
    
    plt.legend([yearsList[2],yearsList[1],str(yearsList[0]) + " (YTD)"])
    plt.xlabel('\n'+'Test Centers', fontsize=25, weight = "bold")
    plt.ylabel('Number of Students', fontsize=25, weight = "bold")
    plt.title('Count of Students at each Center for Last 3 Years'+"\n", fontsize=35, weight = "bold")

    #Save the Pie Chart image to respective report directory
    #Absolute path of report directory
    abs_path = os.path.abspath(os.path.dirname(__file__))
    rel_path = "output"
    path = os.path.join(abs_path, rel_path)
    if not os.path.exists(path):
        os.makedirs(path)
    yearRange = str(yearsList[2]) + '-' + str(yearsList[0])
    file_name = 'Student_Distribution_BarPlot_' + yearRange +'.png'
    #plt.figure(figsize=(20,20))
    my_dpi = 72        
    plt.savefig(os.path.join(path, file_name), dpi = my_dpi)
#    plt.savefig('Student_Distribution_BarPlot_' + yearRange +'.png')
    plt.show()

    image_path_input = path
    image_path_output = path
    fnt = ImageFont.truetype("arial.ttf", 25)
    image_name_input = '\\' + file_name
    today = date.today()
    im = Image.open(image_path_input + image_name_input)
    position = (1130, 1230)
    message = today.strftime("%m/%d/%Y")
    
    # initialise the drawing context with the image object as background
    draw = ImageDraw.Draw(im)
    draw.text(position, message, font = fnt, fill = "black")
    
    im.show()
    image_name_output = '\\' + file_name
    im.save(image_path_output + image_name_output)

    