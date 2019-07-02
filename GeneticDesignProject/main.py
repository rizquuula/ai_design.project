import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image, ImageFilter

#Import other python program
from Algorithm_Crop1x1 import crop1x1
from Histogram import BGR_hist

img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example2.jpg",1)
original_img = img
img = crop1x1(img,600)#max(img.shape[:2]))
# img = cv2.copyMakeBorder(img, 100,100,100,100,cv2.BORDER_CONSTANT,value = [0,0,0])
# print(img.shape[:2]) #print 2 first array
img_width = img.shape[1]
img_height = img.shape[0]

## Draw text in simple way
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(img_height//2,img_width//4), font, 4,(255,255,255),2,cv2.LINE_AA)

FONT_PATH = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/IndieFlower.ttf'
FONT_SIZE = 100
font = ImageFont.truetype(FONT_PATH,FONT_SIZE)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)

TEXT = "LinkGish"
textsize = font.getsize(TEXT)       #Getting the width of the text
print('Text size = ',textsize)
# print(len(TEXT)) #Count word in TEXT
PLACE_X = (img_width-textsize[0])//2
PLACE_Y = (img_height-textsize[1])//4

draw.text((PLACE_X,PLACE_Y), TEXT, font = font, fill = BGR_hist(img))#(b, g, r, a))
print('shape 1 = ',draw.shape)
print('shape 2 = ',img.shape)
# print('shape 3 = ',img_pil.shape) #Err
img = np.array(img_pil)

# cv2.imshow('Original img', original_img)
cv2.imshow('Result',img)
cv2.waitKey(0)