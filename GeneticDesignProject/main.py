import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image, ImageFilter

#Import other python program
from Algorithm_Crop1x1 import crop1x1_cv2
from Histogram import BGRA_hist, Offset_hist, BW_hist, BGR_hist, Offset_histBGR
from Algorithm_Text import TextDrawShade, drawTitle
from Algorithm_BodyText import MakeBodyText
from Algorithm_BackgroundManipulation import GammaCorrection
from Algorithm_Sosmed import drawIGaccount, drawAnotherSosmed

#Open image using OpenCV /  cv2
img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/example3.jpg")
original_img = img #Save original image on a fix variable
img = GammaCorrection(image=img,
                        gamma=5)
img_size = 2000
img = crop1x1_cv2(img,img_size)  #Crop the image in square dimension
#Save it to a file from cv2
#So it can be edited by PIL soon
cv2.imwrite('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/crop1x1_cv2.jpg',img) 

#MAke overlay image using PIL
# overlay_img = Image.new("RGB", img.shape[:2],('black'))# color=Offset_hist(BGRA_hist(img))) #Use shape[:2] because PIL only edit 2D image
#square image so..
# img_width, img_height = img_size, img_size
#Open cropped image using PIL
TITLE_TEXT = 'Berubahlah,-'
masked_img = Image.open("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/crop1x1_cv2.jpg")

drawTitle = drawTitle(fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/IndieFlower/IndieFlower.ttf',
    fontSize = 400,
    text = TITLE_TEXT,
    )
ratio = (masked_img.size[0]/3)/masked_img.size[0]
drawTitle = drawTitle.resize((int(drawTitle.size[0]*ratio), int(drawTitle.size[1]*ratio)) ,Image.ANTIALIAS)
masked_img.paste(drawTitle,((masked_img.size[0]-drawTitle.size[0])//2, masked_img.size[1]//4),drawTitle)

# body_text.show()
# masked_img.save('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultTitleImage.jpg')
# masked_img.show()
# img = np.array(masked_img)
result_img = masked_img#Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultTitleImage.jpg')
#Make body text
typedBodyText = "'Allah tidak akan mengubah keadaan suatu kaum, sampai mereka mengubah apa yang ada pada diri mereka sendiri.'"
BodyFont = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Comfortaa/Comfortaa-Bold.ttf'
body_text = MakeBodyText(size=(2000,2000),
                        text=typedBodyText,
                        FONT_PATH=BodyFont,
                        FONT_SIZE=200,
                        wrap_width=30,
                        padding=10,
                        # rect_fill=(BGR_hist(original_img),150),
                        font_color=(255,255,255,255),
                        isBackRect=False,
                        )
                        
numberOfLine = body_text[1]
body_text = body_text[0]
# body_text.show()
# print(numberOfLine)
desiredHeight = (result_img.size[1]//30) * numberOfLine
# print(desiredHeight)
ratioBodyText = desiredHeight/body_text.size[1]
# print(ratioBodyText)
newBodyTextSize = int(body_text.size[0]*ratioBodyText), int(body_text.size[1]*ratioBodyText)
# print(newBodyTextSize)
body_text = body_text.resize(newBodyTextSize, Image.ANTIALIAS)
# body_text.show()

result_img.paste(body_text,((result_img.size[0]-body_text.size[0])//2, ((result_img.size[1]//4)+drawTitle.size[1]+(result_img.size[1]//30))),body_text)
result_img = drawIGaccount(backgroundImg=result_img,
                            instaAccount='@AiDesain')
result_img =drawAnotherSosmed(image=result_img,
                    account_IG = '@rzf.gsh',
                    account_FB = 'M Razif Rizqullah',
                    account_WA = None,
                    account_LINE = 'r.linkgish',
                    account_TELEGRAM = None,
                    account_WEB = 'www.aidesign.id',
                    account_TWITTER = '@linkgish',
                    account_YOUTUBE = None)
result_img.save('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultImage.jpg')
result_img.show()