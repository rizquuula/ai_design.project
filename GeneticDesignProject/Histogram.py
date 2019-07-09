from matplotlib import pyplot as plt
import cv2 
import numpy as np 

def returntest(number):     
    #Just checking the return function
    a = number[0]
    b = number[1]
    c = number[2]
    return a,c,b

def BW_hist(img_source):
    # Histogram black white
    plt.hist(img_source.ravel(),256,[0,256])
    # plt.show()

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
    b, g, r, a = ValColorDominant,ValColorDominant,ValColorDominant, 1
    return b, g, r, a

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

