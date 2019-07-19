import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image, ImageFilter

#Import other python program
from Algorithm_Crop1x1 import crop1x1_cv2
from Histogram import BGRA_hist, Offset_hist, BW_hist, BGR_hist, Offset_histBGR
from Algorithm_Text import TextDrawShade, drawTitle
from Algorithm_BodyText import MakeBodyText
from Algorithm_BackgroundManipulation import GammaCorrection, whatsGamma
from Algorithm_Sosmed import drawIGaccount, drawAnotherSosmed
from Algorithm_backgroundSelection import backgroundSelection

#Open image using OpenCV /  cv2
# img = cv2.imread("/Image-lib/3.jpg")

img = backgroundSelection(category='City').convert('RGB')
img = np.array(img)
img = img[:, :, ::-1].copy() 
gammaIs = whatsGamma(img)
img = GammaCorrection(image=img,
                        gamma=gammaIs)
img_size = 2000
img = crop1x1_cv2(img,img_size)  #Crop the image in square dimension
#Save it to a file from cv2
#So it can be edited by PIL soon
# cv2.imwrite('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/crop1x1_cv2.jpg',img) 
masked_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
masked_img = Image.fromarray(masked_img)
#MAke overlay image using PIL
# overlay_img = Image.new("RGB", img.shape[:2],('black'))# color=Offset_hist(BGRA_hist(img))) #Use shape[:2] because PIL only edit 2D image
#square image so..
# img_width, img_height = img_size, img_size
#Open cropped image using PIL
TITLE_TEXT = "Don't Ever GIVE UP!"
# masked_img = Image.open("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/crop1x1_cv2.jpg")

drawTitle = drawTitle(fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Kaushan_Script/KaushanScript-Regular.ttf',
    fontSize = 400,
    text = TITLE_TEXT,
    blurRad=20,
    shadowColor=(0,0,0,200),
    )

ratio = (masked_img.size[0]/2)/drawTitle.size[0]
drawTitle = drawTitle.resize((int(drawTitle.size[0]*ratio), int(drawTitle.size[1]*ratio)) ,Image.ANTIALIAS)
# drawTitle.show()
masked_img.paste(drawTitle,((masked_img.size[0]-drawTitle.size[0])//2, masked_img.size[1]//4),drawTitle)

# body_text.show()
# masked_img.save('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultTitleImage.jpg')
# masked_img.show()
# img = np.array(masked_img)
result_img = masked_img#Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultTitleImage.jpg')
#Make body text
typedBodyText = "“Pernah ngga, sudah berusaha keras, mencoba mengejar suatu hal, meski sekuat tenaga tapi belum memperolehnya? Jangan berbalik! Kesuksesan itu menunggumu pantas untuk mendapatkannya.”"
BodyFont = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Marck_Script/MarckScript-Regular.ttf'
body_text = MakeBodyText(size=(2000,2000),
                        text=typedBodyText,
                        FONT_PATH=BodyFont,
                        FONT_SIZE=200,
                        wrap_width=30,
                        padding=10,
                        # isBackRect=True,
                        # rect_fill=(255,255,255,180),
                        font_color=(255,255,255,255),
                        # isBackRect=False,
                        )

numberOfLine = body_text[1]
body_text = body_text[0]
body_text = TextDrawShade(size=body_text.size,
                # font=font,
                image=body_text,
                # text=text,
                placex=0,
                placey=0,
                fill=(0,0,0,255),
                radius=20,
                margin=5
                )

# body_text.show()
# print(numberOfLine)
desiredHeight = (result_img.size[1]//20) * numberOfLine
print(desiredHeight,' from ', numberOfLine, ' and ', (result_img.size[1]//20))
ratioBodyText = desiredHeight/body_text.size[1]
# print(ratioBodyText)
newBodyTextSize = int(body_text.size[0]*ratioBodyText), int(body_text.size[1]*ratioBodyText)
# print(newBodyTextSize)
body_text = body_text.resize(newBodyTextSize, Image.ANTIALIAS)
# body_text.show()

result_img.paste(body_text,((result_img.size[0]-body_text.size[0])//2, ((result_img.size[1]//4)+drawTitle.size[1]+(result_img.size[1]//30))),body_text)
result_img = drawIGaccount(backgroundImg=result_img,
                            fontPath='/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-BoldItalic.ttf',
                            instaAccount='@Rzf.Gsh')
result_img =drawAnotherSosmed(image=result_img,
                    account_IG = '@rzf.gsh',
                    account_FB = 'M Razif Rizqullah',
                    account_WA = None,
                    account_LINE = 'r.linkgish',
                    account_TELEGRAM = None,
                    account_WEB = None,
                    account_TWITTER = '@linkgish',
                    account_YOUTUBE = 'Razif Rizqullah')

#Copyright
subsFont = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-RegularItalic.ttf'   #Open custom font
subs_font = ImageFont.truetype(subsFont,100)
copyRight = 'Generated by AiDesign'
textSize = subs_font.getsize(copyRight)
canvas = Image.new('RGBA', textSize)
draw = ImageDraw.Draw(canvas)
draw.text((0,0),copyRight, fill='white',font=subs_font)
ratio = (result_img.size[1]/50)/textSize[1]
newSize = int(textSize[0]*ratio), int(textSize[1]*ratio)
print(newSize)
canvas = canvas.resize(newSize, Image.ANTIALIAS)
print(canvas)
result_img.paste(canvas, (img_size*24//30,(img_size*29//30)), canvas )
result_img.save('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultImage.jpg')
result_img.show()
# print('Done')