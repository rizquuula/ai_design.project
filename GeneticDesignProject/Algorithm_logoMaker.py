from PIL import ImageFont, ImageDraw, Image, ImageFilter
import numpy as np 
from Algorithm_Sosmed import drawHashtag
from Algorithm_Sosmed import drawIGaccount
from Algorithm_colorMaterial import LIGHTorDARK
from Algorithm_BackgroundManipulation import pasteTransparentImage
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
    
    if mdc!= None:
        mdc = logoResizer(logo= mdc, targetHeight=targetHeight)
        totalWidth.append(mdc.size[0]+targetHeight//2)
        logoBox.append(mdc)
    else:
        pass

    if logo3!= None:
        logo3 = logoResizer(logo= logo3, targetHeight=targetHeight*80//100)
        totalWidth.append(logo3.size[0]+targetHeight//2)
        logoBox.append(logo3)
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
biiLogoPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Logo-birohmah.png'
fsldkLogoPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-fsldklampung.png'
unilaLogoPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-unila.png'
def drawOranizerLogo(
                image = None, 
                # image = Image.new('RGBA', (1000,300),'white'),
                logo_1 = None,
                # logo_1 = unilaLogoPath,
                logo_2 = None,
                # logo_2 = biiLogoPath,
                logo_3 = None,
                # logo_3 = fsldkLogoPath,
                logo_4 = None,
                logo_5 = None,
                # sizeXratio = 50,
                sizeYratio = 10,
                pasteXRatio = 10,
                pasteYRatio = 10,
                percentPadding = 10,
                backColor = (222,222,222),
                backTransparency = 10,
                ):
    imageSize = image.size
    logoBox = []
    allPath = [logo_1, logo_2, logo_3, logo_4, logo_5]
    logoW = 0
    logoH = int((sizeYratio/100)*imageSize[1])
    padding = int((percentPadding/100)*logoH)
    for i in  allPath:
        if i != None:
            logo = Image.open(i)
            logo = logoResizer(logo = logo, 
                            targetHeight= logoH)
            logoW += logo.size[0]
            logoBox.append(logo)
    canvas = Image.new('RGBA', (logoW+padding*2, logoH+padding*2), 0)
    # canvas.show()
    backImage = Image.new('RGB', (logoW+padding*2, logoH+padding*2),color = backColor)
    # backImage.show()
    
    pasteW = int((pasteXRatio/100)*imageSize[0])
    pasteH = int((pasteYRatio/100)*imageSize[1])

    canvas = pasteTransparentImage(image=canvas, 
                                overlayImage=backImage,
                                percentTransparency=backTransparency,
                                # pasteX= pasteW,
                                # pasteY= pasteH,
                                )
    # canvas.show()
    pasteX = 0+padding
    for logo in logoBox:
        canvas.paste(logo, (pasteX, 0 + padding), logo)
        pasteX+=(logo.size[0])

    image.paste(canvas, (pasteW, pasteH), canvas)

    return image
    
# drawOranizerLogo().show()


def drawSponsorshipLogo(
                    image = None, #Image.new('RGBA', (1000,300),'white'),
                    logo1 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/a.png',
                    logo3 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/c.png',
                    logo2 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/b.png',
                    logo4 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/d.png',
                    logo5 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/e.jpg',
                    logo6 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/f.png',
                    logo7 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/g.png',
                    logo8 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/h.png',
                    logo9 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/ff.png',
                    logo10 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/gg.png',
                    logo11 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/hh.png',
                    logo12 = None, #'/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/ff.png',
                    logoHratio = 5,
                    logoRow = 2,
                    padding = 10,
                    ratioXpaste = 10,   # top potition
                    ratioYpaste = 90,   # bottom potition
                    fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-Black.ttf',
                    fontSize = 100,
                    ):
    print()
    # Set the height of logo 
    logoHeight = int((logoHratio/100)*image.size[1])
    # logoHeight = logoRow * logoHeight
    print('logoHeight = ',logoHeight)
    # List all possible logo here
    listLogo = [logo1, logo2, logo3, logo4, logo5, logo6, logo7, logo8, logo9, logo10, logo11, logo12]
    # print(listLogo)
    # Here will be the true logo
    logoBox = []
    for logoPath in listLogo:
        if logoPath != None: # If the logo path not None
            logo = Image.open(logoPath).convert('RGBA') # Pre processing before resizing 
            logo = logoResizer(logo = logo, 
                            targetHeight=logoHeight)
            logoBox.append(logo)    # Append to true box
            # print(logo)
    # print()
    # print(logoBox)
    totalLength = 0 # the length if the logo set horizontally
    
    for logo in logoBox:
        totalLength+=logo.size[0]+padding   # Loop to add length each logo and its padding

    logoRowNew = logoRow-0.3    # Trial and error result, get this master key
    wrapLogoLength = int(totalLength/logoRowNew)    # Set the max logo width for looping each row
    print('total and wrap = ',totalLength,wrapLogoLength)
    
    rowLength = 0   # Leng of each row
    logoPasteCanvas = []    # Paste for each row canvas
    for logo in logoBox:
        rowLength+=logo.size[0]+padding     # looping and add length the row
        if rowLength < wrapLogoLength:
            pass    # pass True 

        else:   # When it get false 
            rowLength = rowLength-logo.size[0]-padding  # Fallback the length 
            canvas = Image.new('RGBA', (rowLength, logoHeight), 0)  # Make it as canvas dimension
            logoPasteCanvas.append(canvas)  # Append to logo paste list
            rowLength = 0   # Reset row length
            rowLength+=logo.size[0]+padding # add the last logo processed so it not missing
    
    # Loop break, and the last canvas not set yet, so this will fix it
    canvas = Image.new('RGBA', (rowLength, logoHeight), 0)  
    logoPasteCanvas.append(canvas)  # Last canvas appended
            
    print('logoPasteCanvas = ',logoPasteCanvas)
    
    pasteX = 0  # Paste coordinate for each logo 
    pasteY = 0  # Paste coordinate for each logo 
    i = 0   # Counter 'what row is now processed?' 
    rowLength = 0   # keep this algorithm to set end of the row
    for logo in logoBox:
        canvas = logoPasteCanvas[i] # Pick i-row
        rowLength+=logo.size[0]+padding # Check if it can fit or not
        if rowLength<wrapLogoLength:    # when it can paste in
            
            # print('logo : ',i,rowLength,logo.size[0])
            canvas.paste(logo, (pasteX, pasteY), logo)  # paste process
            pasteX+=logo.size[0]+padding    # adding padding and size to next paste

        else:   # when the rowlength to long
            canvas = logoPasteCanvas[i+1]   # jump over the next canvas
            pasteX = 0  # reset paste coordinate
            canvas.paste(logo, (pasteX, pasteY), logo)  # paste the last one that get false
            i+=1    # switch the row now
            pasteX = logo.size[0]   # set the next paste coordinate according last logo 
            rowLength = 0   # reset row length
            rowLength+=logo.size[0]+padding # add last logo to row length correction

    
    resultX = []    # box for each row length 

    for canvas in logoPasteCanvas:  # just use looping to 
        resultX.append(canvas.size[0])  # append in the box
    
    lastX = np.max(resultX)     # find the max length 
    lastY = logoHeight*logoRow + padding*logoRow    # set the height based on number of row
    print('lastX,lastY = ',lastX,lastY,'&', logoHeight,logoRow, padding,logoRow)
    lastCanvas = Image.new('RGBA', (int(lastX), int(lastY)), 0)   # last canvas to paste the logo row
    lastPasteY = 0  # paste y start from 0
    for logo in logoPasteCanvas:
        lastPasteX = int((lastX - logo.size[0])/2)  # set justify center 
        lastCanvas.paste(logo,(lastPasteX, lastPasteY ),logo)   # paste it
        lastPasteY+=logoHeight+padding  # change to next row paste

    # lastCanvas.show()

    imageXpaste = int(image.size[0]*(ratioXpaste/100))
    imageYpaste = int(image.size[1]*(ratioYpaste/100)) - lastCanvas.size[1]
    image.paste(lastCanvas, (imageXpaste, imageYpaste), lastCanvas)

    # Word sponsored by
    font = ImageFont.truetype(font=fontPath, size=fontSize)
    text = 'SPONSORED BY'
    textSize = font.getsize(text)
    textCanvas = Image.new('RGBA', textSize, 0)
    draw = ImageDraw.Draw(textCanvas)
    draw.text((0,0), text, fill='white', font=font )
    textCanvas = logoResizer(logo = textCanvas,
                                targetWidth = lastCanvas.size[0]//2)
    image.paste(textCanvas,(imageXpaste+lastCanvas.size[0]//4, int(imageYpaste-textCanvas.size[1]*1.3)),textCanvas)

    
    return image

# drawSponsorshipLogo().show()