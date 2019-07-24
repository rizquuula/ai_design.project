from PIL import Image
import os, os.path
import random
import numpy as np 

# This algorithm will select a picture as background with a random number
def backgroundSelection(category = None):
    imgBox = [] #This image boc will store the image for selection
    # Determine each path of each category
    cityPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/City/'
    dawnPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Dawn/'
    duskPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Dusk/'
    nightPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Night/'
    lightPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Light/'
    darkPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Dark/'
    listNature = [dawnPath, duskPath, nightPath]    # Just a multi category for Nature category
    if category == 'Nature':        # If Nature selected so it will draw a random category
        selected = random.randint(0,2)
        path = listNature[selected]
        print('Selected Path = ', path)
    # Option of category and it path
    if category == 'City':
        path = cityPath
    elif category == 'Dawn':
        path = dawnPath
    elif category == 'Dusk':
        path = duskPath
    elif category == 'Night':
        path = nightPath
    elif category == 'Light':
        path = lightPath
    elif category == 'Dark':
        path = darkPath
    else:
        print('Category do not exist. Error (001)')
    # This will filter image by its format so the other non image file will not distrub the randomize section
    validImage = [".jpg", ".jpeg", ".png"]  
    # Import image and store it in the image box
    for image in os.listdir(path):
        extensionImage = os.path.splitext(image)[1]
        if extensionImage.lower() not in validImage:
            continue    #Skip the file that non image format
        imgBox.append(Image.open(os.path.join(path,image)))
    # This is the main part, randomize the image based on the number of it list index
    imgRandom = random.randint(0,len(imgBox)-1)
    print('Selected Image = ', imgBox[imgRandom])   #Print the selected image in Image PIL format
    
    return imgBox[imgRandom]    #Just return the random image

# RUntest 
# backgroundSelection(category='Nature')