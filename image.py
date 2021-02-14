from PIL import Image, ImageDraw, ImageFont
import numpy as np
import math
import textwrap
import re
import sys
import os.path
from os import path

title = ImageFont.truetype('cambria.ttc', 24)
fnt = ImageFont.truetype('cambria.ttc', 12)


file = open("details.txt",'r')
details = file.read().split("2F Big Bootie Mix #")
file.close()

if len(sys.argv) > 1:
    new_file = sys.argv[1]
    if path.exists(new_file):
        for det in details:
            index = "2F Big Bootie Mix #" + det[0:5]
            if index == new_file[4:len(new_file)-4]:
                rest = det[5:len(det)-1]
                rest = rest[2:len(rest)-1]
                #random color and font assignment
                back_color = list(np.random.choice(range(256), size=3))
                luminance = math.sqrt( 0.299 * back_color[0] ** 2 + 0.587 * back_color[1] ** 2 + 0.114 * back_color[2] ** 2)/255
                if luminance > 0.5 :
                    font_color = (0,0,0)
                else:
                    font_color = (255, 255, 255)
                img = Image.new('RGB', (300, 300), color = (back_color[0], back_color[1], back_color[2]))
                d = ImageDraw.Draw(img)
                d.text((10,30), index, font=title, fill=font_color)
                
                #spacing for lines and cutoffs
                y_text = 65
                rest = rest.replace("w/ ", "|w/ ")
                rest = rest.replace("W/ ", "|w/ ")
                feats = rest.split("|")
                for feat in feats:
                    lines = textwrap.wrap(feat, width=50)
                    for line in lines:
                        width, height = fnt.getsize(line)
                        d.text((10,y_text), line, font=fnt, fill=font_color)
                        y_text += height
                    y_text += 5

                img.save('imgs/'+index+'.png')
                quit()
    else:
        print("invalid file")
        quit()
else:
    answer = input("You have not entered a specific file, would you like to create new images for all files? y/n\n")
    if answer == "y" or answer == "yes":
        print("continuing...\n")
    else:
        quit()
            

for det in details:
    #text clipping
    index = "2F Big Bootie Mix #" + det[0:5]
    rest = det[5:len(det)-1]
    rest = rest[2:len(rest)-1]

    #random color and font assignment
    back_color = list(np.random.choice(range(256), size=3))
    luminance = math.sqrt( 0.299 * back_color[0] ** 2 + 0.587 * back_color[1] ** 2 + 0.114 * back_color[2] ** 2)/255
    if luminance > 0.5 :
        font_color = (0,0,0)
    else:
        font_color = (255, 255, 255)
    img = Image.new('RGB', (300, 300), color = (back_color[0], back_color[1], back_color[2]))
    d = ImageDraw.Draw(img)
    d.text((10,30), index, font=title, fill=font_color)
    
    #spacing for lines and cutoffs
    y_text = 65
    rest = rest.replace("w/ ", "|w/ ")
    rest = rest.replace("W/ ", "|w/ ")
    feats = rest.split("|")
    for feat in feats:
        lines = textwrap.wrap(feat, width=50)
        for line in lines:
            width, height = fnt.getsize(line)
            d.text((10,y_text), line, font=fnt, fill=font_color)
            y_text += height
        y_text += 5

    img.save('imgs/'+index+'.png')
