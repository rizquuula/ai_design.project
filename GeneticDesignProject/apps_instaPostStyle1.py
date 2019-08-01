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

img = backgroundSelection(category='Dusk').convert('RGB')
img = np.array(img)
img = img[:, :, ::-1].copy() 
gammaIs = whatsGamma(img)
img = GammaCorrection(image=img,
                        gamma=gammaIs)
img_size = 2000
img = crop1x1_cv2(img,img_size)  #Crop the image in square dimension
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
img = Image.fromarray(img)
TITLE_TEXT = "Sayang-Nya,"
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
typedBodyText = "Diriwayatkan dari Abi Hurairah r.a, dia berkata; telah bersabda Rasulullah saw “Ketika Allah menetapkan penciptaan makhluk, Dia menuliskan dalam kitab-Nya ketetapan untuk diri-Nya sendiri: Sesungguhnya rahmat-Ku (kasih sayang-Ku) mengalahkan murka-Ku” (diriwayatkan oleh Muslim begitu juga oleh al-Bukhari, an-Nasa-i dan Ibnu Majah)"
# BodyFont = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Marck_Script/MarckScript-Regular.ttf'
# fontPath= '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Comfortaa/Comfortaa-Bold.ttf'
img = MakeBodyText(image=img,
                        text=typedBodyText,
                        FONT_PATH='/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Comfortaa/Comfortaa-Bold.ttf',# BodyFont,
                        FONT_SIZE=500,
                        wrap_width=45,
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
                    hashTag= drawHashtag(hashTag='Hadist qudsi'),
                    logo1= drawHashtag(hashTag='Islamic quotes'),
                    targetHeight= int(img.size[1]/15),
                    isLight=True,
                    ratioWidth = 50,
                    ratioHeight = 80,
                    )
                    
img = drawAnotherSosmed(image=img,
                    ratioHeight=2.5,
                    useOverlay=True,
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
# img = cv2.imread(savePath)
# cv2.imshow('res', img)
# cv2.waitKey(0)
