# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:33:08 2019

@author: Harshit
PGM 2
"""

import os
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from datetime import date


def course_distribution_pie(courseWareCNT, blackBoardCNT, yearVal):
    #plt.rcParams['font.size'] = 9.0
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:    
    courseWareCNTVal = courseWareCNT
    blackBoardCNTVal = blackBoardCNT
    testCenters = 'Blackboard', 'CourseWare'
    studCount = [blackBoardCNTVal, courseWareCNTVal]
    explode = (0.1, 0)  # only "explode" the 1st slice (i.e. 'AAH')
    cols = ['c', 'darkorange']
    
    fig1, ax1 = plt.subplots(figsize=(20, 18))
#    fig1.subplots_adjust(left=0.15, bottom=None, right=0.75, top=None, wspace=None, hspace=None)
    
    patches, texts, autotexts = ax1.pie(studCount, 
            explode = explode, 
            labels = testCenters,
            colors = cols,
            shadow = True, 
            startangle = 90,
            autopct = '%1.1f%%', textprops={'fontsize': 30, 'weight': 'bold'})
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    #plt.title('Total count of Students at each Center', fontsize = 30, loc = 'center')
    
    plt.setp(autotexts, size = 30, weight="bold")
    
    if yearVal not in ['all', 'All', 'ALL']:
        ax1.set_title("Blackboard VS CourseWare: "+str(yearVal)+"\n", size = 35, weight = "bold")
    else:
        ax1.set_title("Blackboard VS CourseWare"+"\n", size = 35, weight = "bold")        


    #Save the Pie Chart image to respective report directory
    #Absolute path of report directory
    abs_path = os.path.abspath(os.path.dirname(__file__))
    rel_path = "output"
    path = os.path.join(abs_path, rel_path)
    if not os.path.exists(path):
        os.makedirs(path)
    if yearVal not in ['all', 'All', 'ALL']:
        file_name = 'Course_Distribution_PiePlot_' + yearVal +'.png'
    else:
        file_name = 'Course_Distribution_PiePlot_all.png'

    my_dpi = 72        
    plt.savefig(os.path.join(path, file_name), dpi = my_dpi)    
#    plt.savefig('Course_Distribution_PiePlot_' + yearVal +'.png')
    plt.show()

    image_path_input = path
    image_path_output = path
    fnt = ImageFont.truetype("arial.ttf", 25)
    image_name_input = '\\' + file_name
    today = date.today()
    im = Image.open(image_path_input + image_name_input)
    position = (1250, 1230)
    message = today.strftime("%m/%d/%Y")
    
    # initialise the drawing context with the image object as background
    draw = ImageDraw.Draw(im)
    draw.text(position, message, font = fnt, fill = "black")
    
    im.show()
    image_name_output = '\\' + file_name
    im.save(image_path_output + image_name_output)
