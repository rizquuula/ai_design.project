import cv2 
import numpy as np 
from PIL import ImageFont, ImageDraw, Image, ImageFilter
from time import ctime

from Algorithm_backgroundSelection import backgroundSelection
from Algorithm_Crop1x1 import crop1x1_cv2
from Algorithm_BackgroundManipulation import GammaCorrection, whatsGamma
from Algorithm_drawTitleStyle2 import drawTitleStyle2
from AlgorithmcolorMaterial import random2MaterialColor, selectColor
from Algorithm_Sosmed import drawHashtag, drawIGaccount, drawAnotherSosmed
from Algorithm_CopyRight import drawCopyright
from Algorithm_logoMaker import combineLogo, drawMDClogo, logoResizer


img = backgroundSelection(category='Nature').convert('RGB')
# img = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/City/city-wallpaper-27.jpg')
img = np.array(img)
img = img[:, :, ::-1].copy() 
gammaIs = whatsGamma(img)
img = GammaCorrection(image=img,
                        gamma=gammaIs)
img_size = 2000
img = crop1x1_cv2(img,img_size)  #Crop the image in square dimension
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
img = Image.fromarray(img)

#Making the text
img = drawTitleStyle2(bigText="bersabarlah",
                        littleText='Wahai Hati',
                        imageSource=img,
                        bigTextColor=(255,255,255,255), #selectColor(color='grey'),
                        littleTextColor=(255,224,130),
                        bigFontSize=1300,
                        littleTextSize=500,
                        )

img = drawCopyright(image=img)
img = combineLogo(image=img,
                    mdc=drawMDClogo(),
                    instagram= drawIGaccount(instaAccount='@Rzf.Gsh'),
                    hashTag= drawHashtag(hashTag='Quotes Muslim'),
                    targetHeight= int(img.size[1]/15),
                    )

img = drawAnotherSosmed(image=img,
                    account_IG='@Rzf.Gsh',
                    account_FB='M Razif Rizqullah',
                    account_TELEGRAM='LinkGish',
                    account_WA = None ,
                    account_LINE = None ,
                    account_WEB = None ,
                    account_TWITTER = 'LinkGish',
                    account_YOUTUBE = None,
                    ratioHeight=2,
                    )

nowTime = ctime()

savePath = ('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Result-lib/Style2 {}.jpg').format(nowTime)
img.save(savePath)
print('Successfully saved at : ',savePath)
img.thumbnail((500,500))
img.show()