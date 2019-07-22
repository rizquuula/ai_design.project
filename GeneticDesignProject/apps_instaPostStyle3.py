from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np
import cv2

from Algorithm_backgroundSelection import backgroundSelection
from Algorithm_BackgroundManipulation import GammaCorrection, whatsGamma
from Algorithm_Crop1x1 import crop1x1_cv2

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
print('Background loaded success....')

img.thumbnail((500,500))
img.show()