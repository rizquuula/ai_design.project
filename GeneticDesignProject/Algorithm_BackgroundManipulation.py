import cv2 
import numpy as np 
from matplotlib import pyplot as plt
from random import randint
from PIL import Image
# from Algorithm_logoMaker import imgResizer

# This algorithm will use gamma to dim the background
def GammaCorrection(image=None, gamma=2.5):
    lookUpTable = np.empty((1,256), np.uint8)
    for i in range(256):
        lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)
    res = cv2.LUT(image, lookUpTable)
    
    # if np.shape(image)[2] ==3:
    #     res = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)  
    #     res = Image.fromarray(res)
        
    return (res)

# Determine the gamma level with histogram 
def whatsGamma(img_source = None):
    plt.hist(img_source.ravel(),256,[0,256])
    histr = cv2.calcHist([img_source], [0], None, [256], [0,256]) #Channel set to 0 for Grayscale image

    dark = np.average(histr[:127]) # Dark color area
    light = np.average(histr[127:]) # Bright color area
    ave = np.average(histr) #Average of the histogram, the number should be fixed based on the image resolution
    gamma = ((ave+light)/ave)+0.5   # This is trial and error algorithm, change if there is a better algorithm
    print('Gamma changer algorithm...')
    print('dark = ', dark)
    print('light = ', light)
    # print('ave = ', ave)
    print('gamma = ', gamma)
    # print(np.argmax(histr), histr[np.argmax(histr)])
    # print(np.argmin(histr), histr[np.argmin(histr)])
    # print(np.max(histr),
    #         histr[np.max(histr)])
    # print(np.min(histr),
    #         histr[np.min(histr)])
    # print(np.average(histr))
    # print()
    # Return the gamma level to be used in gamma correction algorithm
    return gamma
    # plt.show()



def makeGradientImage(width = 300,
                        height =300,
                        initialR = None,
                        initialG = None,
                        initialB = None,
                        ):
    if (initialR == None): 
        initialR = randint(50,255)
    
    if (initialG == None):
        initialG = randint(50,255)

    if (initialB == None):
        initialB = randint(50,255)

    print('Each initial color = ',initialR,initialG,initialB)
    img = Image.new('RGBA', (width,height), color=(255,255,255,100))
    pix = img.load()
    # print(pix)

    R = initialR
    for x in range(img.size[0]):
        G =(int(initialG*((x/float(img.size[0]))))) # A % of image width

        for y in range(img.size[1]):
            B = (int(initialB*(1-(y/float(img.size[1]))))) # A % of image height

            pix[x,y] = (R,G,B)
            # print(x,y,pix[x,y])

    return img

# for i in range(5):
#     makeGradientImage().show()

# whiteC = Image.new('RGBA',(500,500),color='white')
# blackC = Image.new('RGBA',(300,300),color='black')
# blueC = Image.new('RGBA',(300,300),color='blue')
# blackC.paste(blueC,(50,50),blueC)
def pasteTransparentImage(image = None,
                overlayImage = None,
                percentTransparency = 50,
                pasteX = 0,
                pasteY = 0,
                ):
    
    if overlayImage.mode !='RGBA':
        alphaLayer = Image.new('L',overlayImage.size, 255)
        overlayImage.putalpha(alphaLayer)

    if overlayImage.size != image.size:
        overlayImage =  imgResizer(img=overlayImage,
                                targetWidth=image.size[0])
    paste_mask = overlayImage.split()[3].point(lambda i: i * percentTransparency / 100.)
    # paste_mask.show()
    # image.show()
    # paste_mask.show()
    image.paste(overlayImage,(pasteX, pasteY),mask=paste_mask)
    return image
# pasteTransparentImage(image=whiteC,
#             overlayImage=blackC).show()

def imgResizer(img = None,
                targetHeight = None,
                targetWidth = None):
    if targetHeight != None:
        ratio = targetHeight/img.size[1]
        newSize = int(ratio*img.size[0]), int(ratio*img.size[1])
        # print ('Resizer (r & res) = ',ratio, newSize)
        img = img.resize(newSize, Image.ANTIALIAS)
        return img 
    elif targetWidth != None:
        ratio = targetWidth/img.size[0]
        newSize = int(ratio*img.size[0]), int(ratio*img.size[1])
        # print ('Resizer (r & res) = ',ratio, newSize)
        img = img.resize(newSize, Image.ANTIALIAS)
        return img 