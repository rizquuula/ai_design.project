
import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image, ImageFilter

#Import other python program
from Algorithm_Crop1x1 import crop1x1_cv2
from Histogram import BGR_hist, Offset_hist, BW_hist
from Algorithm_Text import TextDrawShade

img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example2.jpg",1)
original_img = img
img = crop1x1_cv2(img,600)#max(img.shape[:2]))
cv2.imwrite('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/crop1x1_cv2.jpg',img)
overlay_img = Image.new("RGB", img.shape[:2], color=Offset_hist(BGR_hist(img)))#"orange")  # This could be a bitmap fill too, but let's just make it orange
# img = cv2.copyMakeBorder(img, 100,100,100,100,cv2.BORDER_CONSTANT,value = [0,0,0])
# print(img.shape[:2]) #print 2 first array
img_width = img.shape[1]
img_height = img.shape[0]

# For PIL
img_crop = Image.open("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/crop1x1_cv2.jpg")

## Draw text in simple way
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,'OpenCV',(img_height//2,img_width//4), font, 4,(255,255,255),2,cv2.LINE_AA)

FONT_PATH = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/IndieFlower.ttf'
FONT_SIZE = 100
img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example2.jpg",1)
font = ImageFont.truetype(FONT_PATH,FONT_SIZE)
TEXT = "LinkGish"
textsize = font.getsize(TEXT)   #Getting the width of the text
print('Text size = ',textsize)
# print(len(TEXT)) #Count word in TEXT
PLACE_X = (img_width-textsize[0])//2
PLACE_Y = (img_height-textsize[1])//4
print('PLACE HERE = ',PLACE_X,PLACE_Y)

mask_img = TextDrawShade(size=overlay_img.size,
            font=font,
            text=TEXT,
            placex=PLACE_X,
            placey=PLACE_Y,
            fill=255,
            radius=3         
            )
# print('shape 1 = ',draw.shape)
# print('shape 2 = ',img.shape)
# print('shape 3 = ',img_pil.shape) #Err
# img = np.array(img_pil)

# cv2.imshow('Original img', original_img)
# cv2.imshow('Result',img)
# cv2.waitKey(0)
# mask_img = TextDraw((img_crop.size))
# mask_img = make_ellipse_mask(img_crop.size, 150, 70, 350, 250, 5)
print(overlay_img.size, img_crop.size, mask_img.size)
# overlay_img.show()
# img_crop.show()
# mask_img.show()
masked_img = Image.composite(overlay_img, img_crop, mask_img)
# img = np.array(masked_img)
# masked_img.show()

# array_img = np.array(masked_img)
# title_img = Image.fromarray(array_img)
draw = ImageDraw.Draw(masked_img)
draw.text((PLACE_X,PLACE_Y), TEXT, font = font, fill = BGR_hist(original_img))#(240,240,240,1))#BGR_hist(original_img))#(b, g, r, a))
masked_img.save('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/ResultTitleImage.jpg')
masked_img.show()

# img = np.array(masked_img)
# cv2.imshow('Result',img)
# cv2.waitKey(0)

