import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from PIL import ImageFont, ImageDraw, Image, ImageFilter
from time import ctime

#Import other python program
from Algorithm_Crop1x1 import crop1x1_cv2
# from Histogram import BGRA_hist, Offset_hist, BW_hist, BGR_hist, Offset_histBGR
from Algorithm_Text import TextDrawShade, drawTitle
from Algorithm_BodyText import MakeBodyText
from Algorithm_BackgroundManipulation import GammaCorrection, whatsGamma
from Algorithm_Sosmed import drawIGaccount, drawAnotherSosmed, drawHashtag
from Algorithm_backgroundSelection import backgroundSelection
from Algorithm_CopyRight import drawCopyright
from Algorithm_logoMaker import combineLogo, drawMDClogo, logoResizer
from Algorithm_colorMaterial import LIGHTorDARK, randomMaterialColor

img = backgroundSelection(category='Dawn').convert('RGB')
img = np.array(img)
img = img[:, :, ::-1].copy() 
gammaIs = whatsGamma(img)
img = GammaCorrection(image=img,
                        gamma=gammaIs)
img_size = 2000
img = crop1x1_cv2(img,img_size)  #Crop the image in square dimension
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
img = Image.fromarray(img)
TITLE_TEXT = "Hakikat Ilmu,"
img = drawTitle(fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Kaushan_Script/KaushanScript-Regular.ttf',
                        fontSize = 400,
                        # fontColor= randomMaterialColor(typeColor= LIGHTorDARK(image=img)), 
                        image=img,
                        text = TITLE_TEXT,
                        placeXratio = 50,
                        placeYratio = 30,
                        sizeWratio = 50,
                        sizeHratio = 20,
                        # blurRad=0,
                        # shadowColor= LIGHTorDARK(image=img), # (0,0,0,200),
                        )
# titleDraw = img[1]
# img = img[0]

#Make body text
typedBodyText = "”Barang siapa yang menghendaki kehidupan dunia maka wajib baginya memiliki ilmu, dan barang siapa yang menghendaki kehidupan Akherat, maka wajib baginya memiliki ilmu, dan barang siapa menghendaki keduanya maka wajib baginya memiliki ilmu”. (HR.Tirmidzi)"
BodyFont = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Marck_Script/MarckScript-Regular.ttf'
img = MakeBodyText(image=img,
                        text=typedBodyText,
                        FONT_PATH=BodyFont,
                        FONT_SIZE=500,
                        wrap_width=35,
                        padding=10,
                        # isBackRect=True,
                        # rect_fill=(255,255,255,180),
                        # font_color= LIGHTorDARK(image=img),# (255,255,255,255),
                        # isBackRect=False,
                        textYratio = 35,
                        textXratio = 70,
                        placeYRatio = 40
                        )

img = combineLogo(image=img,
                    mdc=drawMDClogo(),
                    # logo1=drawCustomLogo(logoPath=logo1Path),
                    # logo2=drawCustomLogo(logoPath=logo2Path),
                    # logo3=drawCustomLogo(logoPath=logo3Path),
                    # instagram= drawIGaccount(instaAccount='@Rzf.Gsh'),
                    hashTag= drawHashtag(hashTag='today hadist'),
                    targetHeight= int(img.size[1]/15),
                    isLight=True,
                    ratioWidth = 50,
                    ratioHeight = 80,
                    )
                    
img = drawAnotherSosmed(image=img,
                    ratioHeight=2.5,
                    useOverlay=True,
                    # account_IG = '@rzf.gsh',
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
# img = cv2.imread(savePath)
# cv2.imshow('res', img)
# cv2.waitKey(0)
