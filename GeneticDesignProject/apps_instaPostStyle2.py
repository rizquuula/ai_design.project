import cv2 
import numpy as np 
from PIL import ImageFont, ImageDraw, Image, ImageFilter
from time import ctime

from Algorithm_backgroundSelection import backgroundSelection
from Algorithm_Crop1x1 import crop1x1_cv2
from Algorithm_BackgroundManipulation import GammaCorrection, whatsGamma
from Algorithm_drawTitleStyle2 import drawTitleStyle2
from Algorithm_colorMaterial import randomMaterialColor, selectColor, LIGHTorDARK
from Algorithm_Sosmed import drawHashtag, drawIGaccount, drawAnotherSosmed
from Algorithm_CopyRight import drawCopyright
from Algorithm_logoMaker import combineLogo, drawMDClogo, logoResizer

img = backgroundSelection(category='Nature').convert('RGB') #Select background from random image in a category
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
#Done, now any further code is using PIL instead
#Making the big text, and small text
maroon = '#FFA781'
img = drawTitleStyle2(bigText="istiqomah,", 
                        littleText='Kamu Pasti Kuat,.',
                        imageSource=img,
                        bigTextColor= LIGHTorDARK(image=img),#, #selectColor(color='grey'),
                        littleTextColor=randomMaterialColor(typeColor= LIGHTorDARK(image=img)), 
                        bigFontSize=1300,
                        littleTextSize=500,
                        )
# Draw the copyright section in the bottom right 
img = drawCopyright(image=img)
# Draw some logo in a combination size
img = combineLogo(image=img,
                    mdc=drawMDClogo(),
                    # instagram= drawIGaccount(instaAccount='@Rzf.Gsh'),
                    hashTag= drawHashtag(hashTag='Motivational quotes'),
                    targetHeight= int(img.size[1]/15),
                    isLight=True,
                    )
# Drw socmed account left it None or Blank if there is no account
img = drawAnotherSosmed(image=img,
                    useOverlay=True,
                    account_IG='@Rzf.Gsh',
                    account_FB='M Razif Rizqullah',
                    account_TELEGRAM='LinkGish',
                    account_WA = None ,
                    account_LINE = None ,
                    account_WEB = None ,
                    account_TWITTER = 'LinkGish',
                    account_YOUTUBE = None,
                    ratioHeight=2,
                    # fontColor=(55,71,79),
                    )
# Use time as a unique file name, so it will not be duplicated in the future
nowTime = ctime()
# Input variable of time into the string 
savePath = ('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Result-lib/Style2 {}.jpg').format(nowTime)
img.save(savePath)
print('Successfully saved at : ',savePath) # Notification while done
img.thumbnail((500,500))    # Just show thumbnail instead of full size image, because we should keep the quality
img.show() #Show the result