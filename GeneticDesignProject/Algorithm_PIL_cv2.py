import cv2
from PIL import Image
import numpy as np

def PILtoCV2(image = None):
    image = np.array(image)
    image = image[:, :, ::-1].copy() 
    return image

def CV2toPIL(image=None):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
    image = Image.fromarray(image)
    return image