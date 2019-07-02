from matplotlib import pyplot as plt
import cv2 
import numpy as np 

def returntest(number):
    a = number[0]
    b = number[1]
    c = number[2]
    return a,c,b

# cek = returntest([12,23,34])
# print(cek)

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
        # print(histr)
        print(i,' adalah ', np.max(histr), ' di ',np.argmax(histr))
        ColorDominant.append(np.argmax(histr))
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    # plt.show()

    ValColorDominant = np.max(ColorDominant)
    b, g, r, a = ValColorDominant,ValColorDominant,ValColorDominant, 255
    return b, g, r, a
