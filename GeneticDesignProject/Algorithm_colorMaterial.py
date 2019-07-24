import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import cv2
from matplotlib import pyplot as plt
import numpy as np

# Light material color 
red = (239, 83, 80)
pink = (236, 64, 122)
purple = (171, 71, 188)
deep_purple = (126, 87, 194)
indigo = (92, 107, 192)
blue = (66, 165, 245)
light_blue = (41, 182, 246)
cyan = (38, 198, 218)
teal = (38, 166, 154)
green = (102, 187, 106)
light_green = (156, 204, 101)
lime = (212, 225, 87)
yellow = (255, 238, 88)
amber = (255, 202, 40)
orange = (255, 167, 38)
deep_orange = (255, 112, 67)
brown = (141, 110, 99)
grey = (255,255,255)#(189, 189, 189)
blue_grey = (120, 144, 156)

# Dark material color
red800 = (198,40,40)
pink800 = (173,20,87)  
purple800 = (106,27,154)
deepPurple800 = (69,39,160)
indigo800 =(40,53,147)
blue800 = (21,101,192)
lightBlue800 = (2,119,189)
cyan800 = (0,131,143)
teal800 = (0,105,92)
green800 = (46,125,50)
lightGreen800 = (85,139,47)
lime800 = (158,157,36)
yellow800 = (249,168,37)
amber800 = (255,143,0)
orange800 = (239,108,0)
deepOrange800 = (216,67,21)
brown800 = (78,52,46)
grey800 = (66,66,66)
blueGrey800 = (55,71,79)

# Function to ram=ndomize the color from database
def randomMaterialColor(typeColor='Light'):
    listLightColor = [red, pink, purple, deep_purple, indigo, blue, light_blue, cyan,
                    teal, green, light_green, lime, yellow, amber, orange, deep_orange,
                    brown, grey, blue_grey]
    listDarkColor = [red800,pink800,purple800,deepPurple800,indigo800, blue800, 
                lightBlue800,cyan800,teal800,green800,lightGreen800,lime800,
                yellow800,amber800,orange800,deepOrange800,brown800,green800,blueGrey800]
    
    if (typeColor == 'Light') or (typeColor == 'light'):
        listColor = listLightColor
    elif (typeColor == 'Dark') or (typeColor == 'dark'):
        listColor = listDarkColor

    count = len(listColor)
    # print(count)
    num = random.randint(0,count-1)
    result = listColor[num]
    print(result)
    return result

# Function to select color form database by it name
def selectColor(color=None):
    listColorStr = ['red', 'pink', 'purple', 'deep_purple', 'indigo', 'blue', 'light_blue', 'cyan',
                    'teal', 'green', 'light_green', 'lime', 'yellow', 'amber', 'orange', 'deep_orange',
                    'brown', 'grey', 'blue_grey']
    listColor = [red, pink, purple, deep_purple, indigo, blue, light_blue, cyan,
                    teal, green, light_green, lime, yellow, amber, orange, deep_orange,
                    brown, grey, blue_grey]
    if color in listColorStr:
        selected = listColorStr.index(color)
        result =  listColor[selected]
    else:
        result = (255,255,255)

    return result

    

# randomMaterialColor()

def LIGHTorDARK(image=None,
            posX = None, posY = None,
            sizeX = None, sizeY = None,
            ):
    print('Auto color BW detection start')
    x1 = posX
    y1 = posY
    x2 = sizeX
    y2 = sizeY
    image = image.crop((x1,y1,x2,y2))
    print('Result crop is = ',image)
    # image.show()

    # image = image.convert('RGB') #Select background from random image in a category
    #there is 4 category City, Dawn, Dusk, Night
    # image = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/City/city-wallpaper-27.jpg')  #Import a single image as background
    #Converting PIL to OpenCV format (2 Dimension to 3 Dimensional Array)
    image = np.array(image)
    image = image[:, :, ::-1].copy() 

    plt.hist(image.ravel(),256,[0,256])
    histr = cv2.calcHist([image], [0], None, [256], [0,256]) #Channel set to 0 for Grayscale image
    dark = np.average(histr[:127])
    light = np.average(histr[127:])
    print('Dark and Light = ',dark,' // ',light)
    if dark>light:
        lightColor = (255,255,255)
        return lightColor
    else:
        darkColor = (55,71,79)
        return darkColor
    
    
