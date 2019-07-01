import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image
from Preprocessing import preprocessing as PP 

# b, g, r, a = 200,200,200,200
img = cv2.imread("example.jpg",1)
original_img = img
# img = PP(img,max(img.shape[:2]))
# img = cv2.copyMakeBorder(img, 100,100,100,100,cv2.BORDER_CONSTANT,value = [0,0,0])
# print(img.shape[:2]) #print 2 first array
img_width = img.shape[1]
img_height = img.shape[0]
## Histogram black white
# plt.hist(img.ravel(),256,[0,256])
# plt.show()
#  
# Histogram full color
color = ('b','g','r')
ColorDominant = []
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    # print(i,' berikut ',np.where(np.max(histr)), np.shape(histr), np.argmax(histr))
    # print(histr)
    print(i,' adalah ', np.max(histr), ' di ',np.argmax(histr))
    ColorDominant.append(np.argmax(histr))
    plt.plot(histr,color = col)
    plt.xlim([0,256])
# plt.show()

ValColorDominant = np.max(ColorDominant)
b, g, r, a = ValColorDominant,ValColorDominant,ValColorDominant, 255

## Draw text in simple way
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(img_height//2,img_width//4), font, 4,(255,255,255),2,cv2.LINE_AA)

FONT_PATH = 'IndieFlower.ttf'
FONT_SIZE = 100
font = ImageFont.truetype(FONT_PATH,FONT_SIZE)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)

TEXT = "LinkGish"
# print(len(TEXT)) #Count word in TEXT
PLACE_X = 100#img_width//2 #-(FONT_SIZE*len(TEXT))
PLACE_Y = img_height//2-(FONT_SIZE//2)

draw.text((PLACE_X,PLACE_Y), TEXT, font = font, fill = (b, g, r, a))
print('shape 1 = ',draw.shape)
print('shape 2 = ',img.shape)
# print('shape 3 = ',img_pil.shape) #Err
img = np.array(img_pil)

cv2.imshow('Original img',original_img)
cv2.imshow('Result',img)
cv2.waitKey(0)