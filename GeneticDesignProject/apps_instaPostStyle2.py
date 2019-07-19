import cv2 
import numpy as np 
from PIL import ImageFont, ImageDraw, Image, ImageFilter

from Algorithm_backgroundSelection import backgroundSelection
from Algorithm_Crop1x1 import crop1x1_cv2
from Algorithm_BackgroundManipulation import GammaCorrection, whatsGamma
from Algorithm_drawTitleStyle2 import drawTitleStyle2
from colorMaterial import random2MaterialColor, selectColor

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

#Making the text
img = drawTitleStyle2(imageSource=img,
                        bigTextColor=selectColor(color='grey'),
                        littleTextColor=selectColor(color='deep_orange'))
img.save('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultImageStyle2.jpg')
img.thumbnail((500,500))
img.show()