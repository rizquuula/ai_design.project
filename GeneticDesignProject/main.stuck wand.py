import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image, ImageFilter

#Wand
from wand.color import Color
from wand.compat import nested
from wand.drawing import Drawing
from wand.image import Image
import wand.display

#Import other python program
from Algorithm_Crop1x1 import crop1x1
from Histogram import BGR_hist, Offset_hist
# from Algorithm_Shadowing import dropShadow, textShadow
from Algorithm_Shadowing import textShadowWand

img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example2.jpg",1)
IMG_PATH = "/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Cropped1x1.jpg"
original_img = img
img = crop1x1(img,600)  #max(img.shape[:2]))
cv2.imwrite('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Cropped1x1.jpg',img)
# img = cv2.copyMakeBorder(img, 100,100,100,100,cv2.BORDER_CONSTANT,value = [0,0,0])
# print(img.shape[:2]) #print 2 first array
img_width = img.shape[1]
img_height = img.shape[0]
# print(str('rgba'+str(BGR_hist(img))))
## Draw text in simple way
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(img_height//2,img_width//4), font, 4,(255,255,255),2,cv2.LINE_AA)

FONT_PATH = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/IndieFlower.ttf'
FONT_SIZE = 100
# font = ImageFont.truetype(FONT_PATH,FONT_SIZE)
# img_pil = Image.fromarray(img)
# draw = ImageDraw.Draw(img_pil)

TEXT = "GiSh"
textsize = (200,50)#font.getsize(TEXT)       #Getting the width of the text
# print('Text size = ',textsize)
# print(len(TEXT)) #Count word in TEXT
PLACE_X = (img_width-textsize[0])//2
PLACE_Y = (img_height-textsize[1])//4
PLACE = (PLACE_X, PLACE_Y)
fillColor = BGR_hist(img)
shadowColor = Offset_hist(fillColor)
output_Path = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/OutputWand.png'
textShadowWand(image=(img_width,img_height),
                filePath= IMG_PATH,
                # filePath= img,
                fontSize = 100,
                place = PLACE,
                inputText = TEXT,
                blur = (10,5),
                fillcolor = fillColor,
                shadowcolor = shadowColor,
                traceback = output_Path)
# OFFSET = 3
# img_pil.show()
# draw.text((PLACE_X,PLACE_Y), TEXT, font = font, fill = BGR_hist(img))   #(b, g, r, a))
# textShadow(img_pil, TEXT, PLACE, OFFSET, font, BGR_hist(img), Offset_hist(BGR_hist(img)))
# img_pil.show()
# print('shape 1 = ',draw.shape)

#draw = dropShadow(draw, imageSize=textsize, imagePlace=(PLACE_X,PLACE_Y))
# print('shape 2 = ',img.shape)
# print('shape 3 = ',img_pil.shape) #Err
# img = np.array(img_pil)

# cv2.imshow('Original img', original_img)
img = cv2.imread(output_Path)
print('shape 4 = ',img.shape)
cv2.imshow('Result',img)
cv2.waitKey(0)
