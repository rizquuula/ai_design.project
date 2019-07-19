from matplotlib import pyplot as plt
import cv2 
import numpy as np 
from Algorithm_Crop1x1 import crop1x1_cv2
from Algorithm_BackgroundManipulation import GammaCorrection

def returntest(number):     
    #Just checking the return function
    a = number[0]
    b = number[1]
    c = number[2]
    return a,c,b

def BW_hist(img_source):
    # Histogram black white
    plt.hist(img_source.ravel(),256,[0,256])
    histr = cv2.calcHist([img_source], [0], None, [256], [0,256]) #Channel set to 0 for Grayscale image
    
    dark = np.average(histr[:127])
    light = np.average(histr[127:])
    ave = np.average(histr)
    gamma = ((ave+light)/ave)+0.5

    print('dark = ', dark)
    print('light = ', light)
    print('ave = ', ave)
    print('gamma = ', gamma)
    # print(np.argmax(histr), histr[np.argmax(histr)])
    # print(np.argmin(histr), histr[np.argmin(histr)])
    # print(np.max(histr),
    #         histr[np.max(histr)])
    # print(np.min(histr),
    #         histr[np.min(histr)])
    # print(np.average(histr))
    print()
    # return gamma
    plt.show()

def BGRA_hist(img_source):
    # Histogram full color
    color = ('b','g','r')
    ColorDominant = []
    for i,col in enumerate(color):
        histr = cv2.calcHist([img_source],[i],None,[256],[0,256])
        # print(i,' berikut ',np.where(np.max(histr)), np.shape(histr), np.argmax(histr))
        # print(histr)  #Print full layer array
        # print(i,' adalah ', np.max(histr), ' di ',np.argmax(histr)) #Print each layer max value
        ColorDominant.append(np.argmax(histr))
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    # plt.show()

    ValColorDominant = np.max(ColorDominant)
    b, g, r, a = ValColorDominant,ValColorDominant,ValColorDominant, 255
    return b, g, r, a

def BGR_hist(img_source):
    # Histogram full color
    color = ('b','g','r')
    ColorDominant = []
    for i,col in enumerate(color):
        histr = cv2.calcHist([img_source],[i],None,[256],[0,256])
        # print(i,' berikut ',np.where(np.max(histr)), np.shape(histr), np.argmax(histr))
        # print(histr)  #Print full layer array
        # print(i,' adalah ', np.max(histr), ' di ',np.argmax(histr)) #Print each layer max value
        ColorDominant.append(np.argmax(histr))
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    # plt.show()

    ValColorDominant = np.max(ColorDominant)
    b, g, r, a = ValColorDominant,ValColorDominant,ValColorDominant, 255
    return b, g, r, a

def Offset_histBGR(BGRA):
    #Offset function for shading option
    if BGRA[0]>=256//2:
        b=50
        g=50
        r=50
    else:
        b=225
        g=225
        r=225
    return b,g,r

def Offset_hist(BGRA):
    #Offset function for shading option
    if BGRA[0]>=256//2:
        b=50
        g=50
        r=50
        a=255
    else:
        b=225
        g=225
        r=225
        a=255
    return b,g,r,a 

# img1 = cv2.imread('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Dawn/fxDfE91.jpg')
# img1 = crop1x1_cv2(img1, 600)
# num1 = BW_hist(img1)
# # print(num1)
# cv2.imshow('result', GammaCorrection(image=img1, gamma=num1))

# # img2 = cv2.imread('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/City/city-wallpaper-43.jpg')
# # img2 = crop1x1_cv2(img2, 600)
# # num2 = BW_hist(img2)
# # # print(num1)
# # cv2.imshow('result2', GammaCorrection(image=img2, gamma=num2))

# # img3 = cv2.imread('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/City/city-wallpaper-44.jpg')
# # img3 = crop1x1_cv2(img3, 600)
# # num3 = BW_hist(img3)
# # # print(num1)
# # cv2.imshow('result3', GammaCorrection(image=img3, gamma=num3))

# cv2.waitKey(0)