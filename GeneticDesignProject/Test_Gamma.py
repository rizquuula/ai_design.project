import cv2 
import numpy as np 
from Algorithm_Crop1x1 import crop1x1_cv2
from Histogram import BGRA_hist, Offset_hist, BW_hist, BGR_hist, Offset_histBGR

img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example.jpg",1)
img = crop1x1_cv2(img,500)
# BW_hist(img)
img2 = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example3.jpg",1)
img2 = crop1x1_cv2(img2,500)
# BW_hist(img2)
gamma = 2.5
lookUpTable = np.empty((1,256), np.uint8)
# print(lookUpTable)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

gamma2 = 2.5
lookUpTable2 = np.empty((1,256), np.uint8)
# print(lookUpTable2)
for i in range(256):
    lookUpTable2[0,i] = np.clip(pow(i / 255.0, gamma2) * 255.0, 0, 255)

res = cv2.LUT(img, lookUpTable)
# BW_hist(res)

res2 = cv2.LUT(img2, lookUpTable2)
# BW_hist(res2)
cv2.imshow('Original 1',img)
cv2.imshow('Original 2',img2)
cv2.imshow('Result 1',res)
cv2.imshow('Result 2',res2)
cv2.waitKey(0)