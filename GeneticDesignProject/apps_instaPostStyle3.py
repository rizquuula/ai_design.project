from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
import cv2
from time import ctime

from Algorithm_backgroundSelection import backgroundSelection
from Algorithm_BackgroundManipulation import GammaCorrection, whatsGamma
from Algorithm_Crop1x1 import crop1x1_cv2
from Algorithm_BodyText import makeBodyTextNano2
from Algorithm_Sosmed import drawHashtag, drawIGaccount, drawAnotherSosmed
from Algorithm_CopyRight import drawCopyright
from Algorithm_logoMaker import combineLogo, drawMDClogo, logoResizer, drawCustomLogo

img = backgroundSelection(category='Dawn').convert('RGB') #Select background from random image in a category
#there is 4 category City, Dawn, Dusk, Night
# img = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/City/city-wallpaper-27.jpg')  #Import a single image as background
#Converting PIL to OpenCV format (2 Dimension to 3 Dimensional Array)
img = np.array(img)
img = img[:, :, ::-1].copy() 
#Gamma correction using openCV
gammaIs = whatsGamma(img)   #Determine the number of gamma correction
img = GammaCorrection(image=img,
                        gamma=gammaIs)  #Apply the gamma correction
img_size = 2000     #Change the image size, so it will be better for uploading
img = crop1x1_cv2(img,img_size)  #Crop the image in square dimension using OpenCV
# Convert OpenCV format to PIL format
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
img = Image.fromarray(img)
print('Background loaded success....')
# Draw the copyright section in the bottom right 
img = drawCopyright(image=img)
# Draw some logo in a combination size
# Logo path to create
logo1Path = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-www.png'
logo2Path = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-whatsapp.png'
logo3Path = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-telegram.png'
img = combineLogo(image=img,
                    mdc=drawMDClogo(),
                    # logo1=drawCustomLogo(logoPath=logo1Path),
                    # logo2=drawCustomLogo(logoPath=logo2Path),
                    # logo3=drawCustomLogo(logoPath=logo3Path),
                    # instagram= drawIGaccount(instaAccount='@Rzf.Gsh'),
                    hashTag= drawHashtag(hashTag='baik berisik'),
                    targetHeight= int(img.size[1]/15),
                    isLight=True,
                    ratioWidth = 50,
                    ratioHeight = 80,
                    )
# Drw socmed account left it None or Blank if there is no account

img = drawAnotherSosmed(image=img,
                    account_IG='@Rzf.Gsh',
                    account_FB='M Razif Rizqullah',
                    # account_TELEGRAM='LinkGish',
                    # account_WA = '082238639221' ,
                    # account_LINE = 'r.linkgish' ,
                    # account_WEB = 'linkgish.com' ,
                    account_TWITTER = 'LinkGish',
                    # account_YOUTUBE = 'M Razif Rizqullah',
                    ratioHeight=2.5,
                    useOverlay= True,
                    # fontColor=(55,71,79),

                    )

img = makeBodyTextNano2(image=img,
                    fontPath= '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Comfortaa/Comfortaa-Bold.ttf',
                    text="Pulau asal kita sama. Pulau tujuan kita sama. Yang membedakan hanya jembatannya saja,.",
                    placeXRatio=25,
                    placeYRatio=40,
                    fieldXRatio=50,
                    fieldYRatio=50,
                    fontSize=100,
                    wrapWidth=25,
                    # typeColor=whatsColoris,
                    )
nowTime = ctime()
# Input variable of time into the string 
savePath = ('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Result-lib/instaStyle3/Style3 {}.jpg').format(nowTime)
img.save(savePath)
print('Successfully saved at : ',savePath) # Notification while done
# img = Image.open(savePath)
img.thumbnail((500,500))    # Just show thumbnail instead of full size image, because we should keep the quality
img.show() #Show the result
# img = cv2.imread(savePath)
# cv2.imshow('res', img)
# cv2.waitKey(0)
