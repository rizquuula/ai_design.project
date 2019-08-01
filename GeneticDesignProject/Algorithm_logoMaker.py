from PIL import ImageFont, ImageDraw, Image, ImageFilter
import numpy as np 
from Algorithm_Sosmed import drawHashtag
from Algorithm_Sosmed import drawIGaccount
from Algorithm_colorMaterial import LIGHTorDARK
# import cv2
pathLogo_MDC = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-MDC-Fit.png'

def drawCustomLogo(logoPath = None,
                targetHeight = 500,
                ):
    CustomLogo = Image.open(logoPath).convert('RGBA')

    overlayColor = Image.new('RGBA',(CustomLogo.size),color='white')
    
    CustomLogoWhite = Image.composite(overlayColor,CustomLogo,CustomLogo)
    
    ratio = targetHeight/CustomLogoWhite.size[1]
    newSize = int(ratio*CustomLogoWhite.size[0]), int(ratio*CustomLogoWhite.size[1])
    CustomLogoWhite = CustomLogoWhite.resize(newSize, Image.ANTIALIAS)
    print('Logo size = ',CustomLogoWhite.size)
    
    return CustomLogoWhite


def drawMDClogo(logoPath = pathLogo_MDC,
                targetHeight = 500,
                ):
    # print(logoPath)
    
    # Finding size only

    # img = cv2.imread(logoPath)
    # cv2.imshow('RAW', img)
    # cv2.waitKey(0)

    # x1 x2 - y1 y2
    # 180 767 - 90 570
    

    mdc = Image.open(logoPath)
    overlayColor = Image.new('RGBA',(mdc.size),color='white')
    mdcWhite = Image.composite(overlayColor,mdc,mdc)
    ratio = targetHeight/mdcWhite.size[1]
    newSize = int(ratio*mdcWhite.size[0]), int(ratio*mdcWhite.size[1])
    mdcWhite = mdcWhite.resize(newSize, Image.ANTIALIAS)
    # mdcWhite = mdcWhite.crop((178, 92, 767, 570))
    # savePath = ('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Result-lib/logo-MDC-Fit.png')
    # mdcWhite.save(savePath)
    
    # mdcWhite.show()
    print('Logo MDC size = ',mdcWhite.size)
    return mdcWhite
# drawMDClogo()

def logoResizer(logo = None,
                targetHeight = None,
                targetWidth = None):
    if targetHeight != None:
        ratio = targetHeight/logo.size[1]
        newSize = int(ratio*logo.size[0]), int(ratio*logo.size[1])
        logo = logo.resize(newSize, Image.ANTIALIAS)
        return logo 
    elif targetWidth != None:
        ratio = targetWidth/logo.size[0]
        newSize = int(ratio*logo.size[0]), int(ratio*logo.size[1])
        logo = logo.resize(newSize, Image.ANTIALIAS)
        return logo 

def imgResizer(img = None,
                targetHeight = None,
                targetWidth = None):
    if targetHeight != None:
        ratio = targetHeight/img.size[1]
        newSize = int(ratio*img.size[0]), int(ratio*img.size[1])
        print ('Resizer (r & res) = ',ratio, newSize)
        img = img.resize(newSize, Image.ANTIALIAS)
        return img 
    elif targetWidth != None:
        ratio = targetWidth/img.size[0]
        newSize = int(ratio*img.size[0]), int(ratio*img.size[1])
        print ('Resizer (r & res) = ',ratio, newSize)
        img = img.resize(newSize, Image.ANTIALIAS)
        return img 

def combineLogo(image = None,
                targetHeight = 100,
                mdc = None,
                logo1 = None,
                logo2 = None,
                logo3 = None,
                hashTag = None,
                instagram = None,
                ratioWidth = 50,
                ratioHeight = 75,
                isLight=True,       # Activate auto coloring 
                overlayColor= (55,71,79),
                ):
    
    logoBox = []
    totalWidth = []
    if logo1!= None:
        logo1 = logoResizer(logo= logo1, targetHeight=targetHeight*80//100)
        totalWidth.append(logo1.size[0]+targetHeight//2)
        logoBox.append(logo1)
    else:
        pass

    if logo2!= None:
        logo2 = logoResizer(logo= logo2, targetHeight=targetHeight*80//100)
        totalWidth.append(logo2.size[0]+targetHeight//2)
        logoBox.append(logo2)
    else:
        pass

    if logo3!= None:
        logo3 = logoResizer(logo= logo3, targetHeight=targetHeight*80//100)
        totalWidth.append(logo3.size[0]+targetHeight//2)
        logoBox.append(logo3)
    else:
        pass

    if mdc!= None:
        mdc = logoResizer(logo= mdc, targetHeight=targetHeight)
        totalWidth.append(mdc.size[0]+targetHeight//2)
        logoBox.append(mdc)
    else:
        pass

    if instagram!=None:
        instaNew = Image.new('RGBA', instagram.size, 0)
        instaNew.paste(instagram, (0,instagram.size[1]//13), instagram)
        instagram = logoResizer(logo= instaNew, targetHeight=targetHeight)
        totalWidth.append(instagram.size[0]+targetHeight//2)
        logoBox.append(instagram)
    else:
        pass

    if hashTag!=None:
        hashTag = logoResizer(logo= hashTag, targetHeight=targetHeight*80//100)
        totalWidth.append(hashTag.size[0]+targetHeight//2)
        logoBox.append(hashTag)
    else:
        pass
    
    
    # mdc.show()
    # hashTag.show()
    # instagram.show()
    canvas = Image.new('RGBA', (np.sum(totalWidth)-targetHeight//2, targetHeight), 0)
    currentPasteWidth = 0
    for logo in logoBox:
        canvas.paste(logo,(currentPasteWidth, 0),logo)
        currentPasteWidth+=logo.size[0]+targetHeight//2
    # canvas.show()
    
    if image!=None:
        if isLight==True:
            placeW, placeH = (image.size[0]-canvas.size[0])*ratioWidth//100, image.size[1]*ratioHeight//100
            autoOverlayColor = LIGHTorDARK(image=image,
                                    posX=placeW,posY=placeH,
                                    sizeX=canvas.size[0],sizeY=canvas.size[1]
                                    )

            darkC = Image.new('RGBA',canvas.size,color=autoOverlayColor)
            canvas = Image.composite(darkC, canvas, canvas)            
            image.paste(canvas,(placeW, placeH),canvas)

            return image
        else:
            #Paste code to background
            # ratio = targetHeight/canvas.size[1]
            # size = int(canvas.size[0]*ratio), int(canvas.size[1]*ratio)
            # canvas = canvas.resize(L_size, Image.ANTIALIAS)
            placeW, placeH = (image.size[0]-canvas.size[0])*ratioWidth//100, image.size[1]*ratioHeight//100
            image.paste(canvas,(placeW, placeH),canvas)

            return image
    
    else: 
        return canvas


# combineLogo(mdc = drawMDClogo(),#targetHeight = targetHeight)
#                 hashTag = drawHashtag(), #targetHeight=targetHeight)
#                 instagram = drawIGaccount(instaAccount='@Ai.Design'))
