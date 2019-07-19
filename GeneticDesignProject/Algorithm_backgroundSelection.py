from PIL import Image
import os, os.path
import random
import numpy as np 


def backgroundSelection(category = None):
    imgBox = []
    cityPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/City/'
    dawnPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Dawn/'
    duskPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Dusk/'
    nightPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/background-lib/Night/'

    listNature = [dawnPath, duskPath, nightPath]
    if category == 'Nature':
        selected = random.randint(0,2)
        path = listNature[selected]
        print('Selected Path = ', path)

    if category == 'City':
        path = cityPath
    elif category == 'Dawn':
        path = dawnPath
    elif category == 'Dusk':
        path = duskPath
    elif category == 'Night':
        path = nightPath
    
    validImage = [".jpg", ".jpeg", ".png"]

    for image in os.listdir(path):
        extensionImage = os.path.splitext(image)[1]
        if extensionImage.lower() not in validImage:
            continue
        imgBox.append(Image.open(os.path.join(path,image)))

    imgRandom = random.randint(0,len(imgBox)-1)
    print('Selected Image = ', imgBox[imgRandom])
    return imgBox[imgRandom]

# backgroundSelection(category='Nature')