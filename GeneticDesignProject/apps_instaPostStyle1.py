import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image, ImageFilter
from time import ctime

#Import other python program
from Algorithm_Crop1x1 import crop1x1_cv2
from Histogram import BGRA_hist, Offset_hist, BW_hist, BGR_hist, Offset_histBGR
from Algorithm_Text import TextDrawShade, drawTitle
from Algorithm_BodyText import MakeBodyText
from Algorithm_BackgroundManipulation import GammaCorrection, whatsGamma
from Algorithm_Sosmed import drawIGaccount, drawAnotherSosmed
from Algorithm_backgroundSelection import backgroundSelection
from Algorithm_CopyRight import drawCopyright

img = backgroundSelection(category='City').convert('RGB')
img = np.array(img)
img = img[:, :, ::-1].copy() 
gammaIs = whatsGamma(img)
img = GammaCorrection(image=img,
                        gamma=gammaIs)
img_size = 2000
img = crop1x1_cv2(img,img_size)  #Crop the image in square dimension
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
img = Image.fromarray(img)
TITLE_TEXT = "Don't Ever GIVE UP!"
img = drawTitle(fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Kaushan_Script/KaushanScript-Regular.ttf',
                        fontSize = 400,
                        image=img,
                        text = TITLE_TEXT,
                        blurRad=20,
                        shadowColor=(0,0,0,200),
                        )
titleDraw = img[1]
img = img[0]

#Make body text
typedBodyText = "“Pernah ngga, sudah berusaha keras, mencoba mengejar suatu hal, meski sekuat tenaga tapi belum memperolehnya? Jangan berbalik! Kesuksesan itu menunggumu pantas untuk mendapatkannya.”"
BodyFont = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Marck_Script/MarckScript-Regular.ttf'
body_text = MakeBodyText(size=img.size,
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
# body_text.show()
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
desiredHeight = (img.size[1]//20) * numberOfLine
print(desiredHeight,' from ', numberOfLine, ' and ', (img.size[1]//20))
ratioBodyText = desiredHeight/body_text.size[1]
newBodyTextSize = int(body_text.size[0]*ratioBodyText), int(body_text.size[1]*ratioBodyText)
body_text = body_text.resize(newBodyTextSize, Image.ANTIALIAS)

img.paste(body_text,((img.size[0]-body_text.size[0])//2, ((img.size[1]//4)+titleDraw.size[1]+(img.size[1]//30))),body_text)

img = drawIGaccount(backgroundImg=img,
                instaAccount='@Rzf.Gsh',
                )

img = drawAnotherSosmed(image=img,
                    ratioHeight=2,
                    account_IG = '@rzf.gsh',
                    account_FB = 'M Razif Rizqullah',
                    account_WA = None,
                    account_LINE = 'r.linkgish',
                    account_TELEGRAM = None,
                    account_WEB = None,
                    account_TWITTER = '@linkgish',
                    account_YOUTUBE = 'Razif Rizqullah')

img = drawCopyright(image=img)

# Use time as a unique file name, so it will not be duplicated in the future
nowTime = ctime()
# Input variable of time into the string 
savePath = ('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Result-lib/Style1 {}.jpg').format(nowTime)
img.save(savePath)
print('Successfully saved at : ',savePath) # Notification while done
img.thumbnail((500,500))    # Just show thumbnail instead of full size image, because we should keep the quality
img.show() #Show the result