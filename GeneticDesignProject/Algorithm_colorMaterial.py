import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import cv2
from matplotlib import pyplot as plt
import numpy as np

# Light material color 
red = (255,205,210)
pink = (248,187,208)
purple = (225,190,231)
deep_purple = (209,196,233)
indigo = (197,202,233)
blue = (187,222,251)
light_blue = (179,229,252)
cyan = (178,235,242)
teal = (178,223,219)

green = (200,230,201)
light_green = (220,237,200)
lime = (240,244,195)
yellow = (255,249,196)
amber = (255,236,179)
orange = (255,224,178)
deep_orange = (255,204,188)
brown = (215,204,200)
grey = (245,245,245)
blue_grey = (207,216,220)

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
    # print(typeColor)
    if (typeColor == 'Light') or (typeColor == 'light') or (typeColor == (255,255,255)):
        listColor = listLightColor
    elif (typeColor == 'Dark') or (typeColor == 'dark') or (typeColor == (55,71,79)):
        listColor = listDarkColor

    count = len(listColor)
    # print(count)
    num = random.randint(0,count-1)
    result = listColor[num]
    print('Random color selected is : ',result)
    return result

# Function to select color form database by it name
def selectColor(color=None):
    listColorStr = ['red', 'pink', 'purple', 'deep_purple', 'indigo', 'blue', 'light_blue', 'cyan',
                    'teal', 'green', 'light_green', 'lime', 'yellow', 'amber', 'orange', 'deep_orange',
                    'brown', 'grey', 'blue_grey']
    listColor = [red, pink, purple, deep_purple, indigo, blue, light_blue, cyan,
                    teal, green, light_green, lime, yellow, amber, orange, deep_orange,
                    brown, grey, blue_grey]
    #Select color by calling it name
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
    
    if posX==None:
        image=image
    else:
        x1,y1,x2,y2 = posX, posY, (posX + sizeX), (posY + sizeY)
        image = image.crop((x1,y1,x2,y2))
        print('Auto color BW detection start with (x1,y1,x2,y2) : ',posX,posY,(posX + sizeX),(posY + sizeY))
    print('Result crop is = ',image)
    # image.show()

    # image = image.convert('RGB') #Select background from random image in a category
    #there is 4 category City, Dawn, Dusk, Night
    # image = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/City/city-wallpaper-27.jpg')  #Import a single image as background
    #Converting PIL to OpenCV format (2 Dimension to 3 Dimensional Array)
    image = image.convert('RGB')
    image = np.array(image)
    image = image[:, :, ::-1].copy() 
    # ploting the Histogram so it can be analyzed
    plt.hist(image.ravel(),256,[0,256])
    histr = cv2.calcHist([image], [0], None, [256], [0,256]) #Channel set to 0 for Grayscale image
    # Describe what is dark and light color, based on their histogram 
    dark = np.average(histr[:150])
    light = np.average(histr[127:])
    print('Dark and Light = ',dark,' // ',light)        # Printing the dark and light param
    if (dark)>light:        # If dark give it light
        lightColor = (255,255,255)
        print('lightColor')
        return lightColor
    else:       # If light give it dark color
        darkColor = (55,71,79)
        print('darkColor')
        return darkColor

def addAlpha(rgb = None,
        alpha = None,
        ):
    RGBA = rgb+(alpha,)
    return RGBA

# rgba = addAlpha(rgb=(1,1,1), alpha=20)
# print(rgba)
