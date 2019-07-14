
import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image, ImageFilter

#Import other python program
from Algorithm_Crop1x1 import crop1x1_cv2
from Histogram import BGRA_hist, Offset_hist, BW_hist, BGR_hist, Offset_histBGR
from Algorithm_Text import TextDrawShade
from Algorithm_BodyText import MakeBodyText
from Algorithm_BackgroundManipulation import GammaCorrection

#Open image using OpenCV /  cv2
img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/example3.jpg",1)
original_img = img #Save original image on a fix variable
img = GammaCorrection(image=img,gamma=3)
img_size = 600
img = crop1x1_cv2(img,img_size)  #Crop the image in square dimension
#Save it to a file from cv2
#So it can be edited by PIL soon
cv2.imwrite('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/crop1x1_cv2.jpg',img) 

#MAke overlay image using PIL
overlay_img = Image.new("RGB", img.shape[:2],('black'))# color=Offset_hist(BGRA_hist(img))) #Use shape[:2] because PIL only edit 2D image
#square image so..
img_width, img_height = img_size, img_size
#Open cropped image using PIL
img_crop = Image.open("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/crop1x1_cv2.jpg")

FONT_PATH = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/IndieFlower/IndieFlower.ttf'   #Open custom font
FONT_SIZE = 40     #Set font size
font = ImageFont.truetype(FONT_PATH,FONT_SIZE,0,"unic",None)  #Generate font
TITLE_TEXT = "Masih Main Aman?"       #Input title text
textsize = font.getsize(TITLE_TEXT)   #Getting the width and height of the text
# print('Text size = ',textsize)  #Checking
PLACE_X = (img_width-textsize[0])//2
PLACE_Y = (img_height-textsize[1])//4
# print('PLACE HERE = ',PLACE_X,PLACE_Y)  #Checking
#Create mask image using other module
mask_img = TextDrawShade(size=overlay_img.size,
            font=font,
            text=TITLE_TEXT,
            placex=PLACE_X,
            placey=PLACE_Y,
            fill=(0,0,0,255),
            radius=5    
            )
# print(overlay_img.size, img_crop.size, mask_img.size) #Checking, all should be same

masked_img = Image.composite(overlay_img, img_crop, mask_img)   #Compose image using PIL
#Draw the image again for create Title Text
draw = ImageDraw.Draw(masked_img)
draw.text((PLACE_X,PLACE_Y), TITLE_TEXT, font = font, fill = 'white') # BGRA_hist(original_img))
# body_text.show()
masked_img.save('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultTitleImage.jpg')
# masked_img.show()
# img = np.array(masked_img)
result_img = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultTitleImage.jpg')
#Make body text
typedBodyText = 'Semua hal memiliki resikonya masing-masing. Dan resiko terbesar akan didapat bila tidak mengambil resiko apapun. Berada di zona nyaman adalah kesalahan terbesar.'
BodyFont = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Comfortaa/Comfortaa-Bold.ttf'
body_text = MakeBodyText(size=masked_img.size,
                        text=typedBodyText,
                        FONT_PATH=BodyFont,
                        FONT_SIZE=20,
                        wrap_width=30,
                        padding=10,
                        # rect_fill=(BGR_hist(original_img),150),
                        font_color=(255,255,255,255),
                        isBackRect=False,
                        )
result_img.paste(body_text,(0,0),body_text)
result_img.save('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultImage.jpg')
result_img.show()

