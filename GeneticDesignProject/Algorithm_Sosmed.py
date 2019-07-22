from PIL import ImageFont, ImageDraw, Image, ImageFilter
import cv2 
import numpy as np

logoIGPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-instagram.png'
backgroundPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/crop1x1_cv2.jpg'
fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-BlackItalic.ttf'   #Open custom font
fontSize = 400     #Set font size
pathLogo_IG = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-instagram.png'
pathLogo_FB = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-facebook.png'
pathLogo_WA = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-whatsapp.png'
pathLogo_LINE = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-line.png'
pathLogo_TELEGRAM = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-telegram.png'
pathLogo_WEB = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-www.png'
pathLogo_TWITTER = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-twitter.png'
pathLogo_YOUTUBE = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-youtube.png'

# Function to draw single IG account for large account sign purpose
def drawIGaccount(logo=logoIGPath,
                    backgroundPath=None,
                    backgroundImg=None,
                    fontPath=fontPath,
                    fontSize=fontSize,
                    instaAccount='@Rzf.Gsh'
                    ):

    logoIG = Image.open(logo)   # Open logo IG from a specified database
    if backgroundImg!=None:
        openImg = backgroundImg     # Open image PIL format
    elif backgroundPath!=None:
        openImg = Image.open(backgroundPath)    # Open file in a path
    else:
        pass # What this is for? hha

    #Create the logo in white color
    OverlayColor = Image.new('RGBA',logoIG.size,'white')
    logoIG_white = Image.composite(OverlayColor, logoIG, logoIG)    # Paste the overlay color
    font = ImageFont.truetype(fontPath,fontSize,0,"unic",None)  #Generate font
    # Input title text
    textsize = font.getsize(instaAccount)   #Getting the width and height of the text
    # print(textsize) 
    # print(logoIG.size) 
    # 
    ratio = (logoIG.size[1]*3/4)/textsize[1] #Ratio
    newTextSize = int(textsize[0]*ratio), int(textsize[1]*ratio)

    newFrameSize = newTextSize[0], int(logoIG.size[0]+newTextSize[1]*3/2)   # Set the size for paste the text and logo
    # print(ratio)
    # This will create the account text 
    textArea = Image.new('RGBA',textsize,color=0)
    drawText = ImageDraw.Draw(textArea)
    drawText.text((0,0), instaAccount, font = font, fill = 'white')
    # textArea.show()
    textArea = textArea.resize((newTextSize), Image.ANTIALIAS)
    # print(textArea.size)

    newFrame = Image.new('RGBA',newFrameSize,color=0)
    newFrame.paste(logoIG_white, (newFrameSize[0]//2-logoIG_white.size[0]//2, 0), logoIG_white)
    newFrame.paste(textArea, (0, int(newTextSize[1]*3/2)), textArea)
    print('logo Instagram size = ', newFrame.size)

    if (backgroundImg == None) and (backgroundPath == None):
        print('No or Fail to load backgroundImg and backgroundPath')
        return newFrame

    targetHeight = openImg.size[1]//15
    ratioOpenImg = targetHeight/newFrame.size[1]
    newSizeForPaste = (int(newFrame.size[0]*ratioOpenImg), int(newFrame.size[1]*ratioOpenImg))

    newFrame = newFrame.resize((newSizeForPaste), Image.ANTIALIAS)

    openImg.paste(newFrame,(openImg.size[0]//2-newFrame.size[0]//2 ,targetHeight*12),newFrame)
    # openImg.show()
    return openImg

    # newFrame.show()
    # logoIG_white.show()
    # textArea.show()

#example, comment this for using the module
# drawIGaccount().show()

def drawAnotherSosmed(#isTrue=False,
                        image=None,
                        backgroundPath=backgroundPath,
                        fontPath=fontPath,
                        fontSize=fontSize,
                        ratioHeight = 5,
                        account_IG = None ,
                        account_FB = None ,
                        account_WA = None ,
                        account_LINE = None ,
                        account_TELEGRAM = None ,
                        account_WEB = None ,
                        account_TWITTER = None,
                        account_YOUTUBE = None,
                    ):
    # IMport background as size reference
    if image==None:
        img = Image.open(backgroundPath)
    else:
        img = image
    
    canvas = Image.new('RGBA',(img.size[0],img.size[1]))
    newCanvas = Image.new('RGBA',(0,0),0)
    # drawOn = ImageDraw.Draw(canvas)
    logoH = img.size[1]*ratioHeight//100
    # What logo will be create next? Make a list first
    listLogoPath = [pathLogo_FB, pathLogo_IG,
                        pathLogo_LINE, pathLogo_TELEGRAM, 
                        pathLogo_TWITTER, pathLogo_WA, 
                        pathLogo_WEB, pathLogo_YOUTUBE]
    listAccount = [account_FB, account_IG,
                    account_LINE, account_TELEGRAM,
                    account_TWITTER, account_WA,
                    account_WEB, account_YOUTUBE]
    
    fullAccCanvas = Image.new('RGBA',(10,10))
    placeX = 0
    placeY = img.size[1]*28//30
    for i in range(len(listAccount)):
        if listAccount[i] != None:
            # print(i,' ada')
            pathLogo = listLogoPath[i]
            logo = Image.open(pathLogo).convert("RGBA")
            
            logoHratio = logoH/logo.size[1]
            logoNewSize = int(logo.size[0]*logoHratio), int(logo.size[1]*logoHratio)
            logo = logo.resize((logoNewSize), Image.ANTIALIAS)
            # logo.show()

            account = listAccount[i]

            font = ImageFont.truetype(fontPath,fontSize,0,"unic",None)  #Generate font
            textsize = font.getsize(account)   #Getting the width and height of the text
            nameAccCanvas = Image.new('RGBA',(textsize[0]+fontSize//3,textsize[1]),0)
            drawNAC = ImageDraw.Draw(nameAccCanvas)
            drawNAC.text((0,0), account, font = font, fill = 'white')
            # nameAccCanvas.show()
            accountRatio = (logoH)/textsize[1]
            accountNewSize = int(textsize[0]*accountRatio), int(textsize[1]*accountRatio)

            nameAccCanvas = nameAccCanvas.resize(accountNewSize,Image.ANTIALIAS)
            # nameAccCanvas.show()
            
            padding = 5
            fullSize = accountNewSize[0]+logoNewSize[0]+padding , logoNewSize[1]
            fullAccCanvas = Image.new('RGBA', fullSize, color=0)
            # drawAC = ImageDraw.Draw(fullAccCanvas) 
            fullAccCanvas.paste(logo, (0,0), logo)
            fullAccCanvas.paste(nameAccCanvas, ((logoNewSize[0]+padding),0), mask=None)
            # fullAccCanvas.show()   
            
            pref_placeX = placeX
            placeX+=fullAccCanvas.size[0]

            
            if placeX>((img.size[0]*2)//3):
                # placeX=0
                placeY+=(logoH)+3
            else:
                pass
            # img.show()
            newCanvas = newCanvas.transform((placeX,logoH), Image.EXTENT, (0,0,placeX, logoH))#(newCanvas.size[0], newCanvas.size[1], placeX, logoH))
            newCanvas.paste(fullAccCanvas,(pref_placeX,0),fullAccCanvas)
            # newCanvas.show()
            # print((img.size[0]*2)//3,' < ',placeX,' & ',placeY)            
            
        else:
            pass
            # print(i,' tak ada')
    # newCanvas = Image.new('RGBA',(img.size),0)
    # newCanvas.paste(canvas,((img.size[0]-placeX)//2,0),canvas)
    # img.paste(canvas,(0,0),canvas)
    # canvas.show()
    centerPaste = (img.size[0]-newCanvas.size[0])//2, int(img.size[1]*26/30)
    print(centerPaste)
    img.paste(newCanvas,(centerPaste),newCanvas)
    # newCanvas.show()
    # img.show()
    return img

'''
drawAnotherSosmed(account_IG = '@rzf.gsh',
                    account_FB = 'M Razif Rizqullah',
                    account_WA = '+62 822 3863 9221',
                    account_LINE = 'r.linkgish',
                    account_TELEGRAM = None,
                    account_WEB = None,
                    account_TWITTER = '@linkgish',
                    account_YOUTUBE = None
                    )'''

def drawHashtag(image = None,
                hashTag = 'Artificial intelligence',
                fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-BoldItalic.ttf',
                fontTagPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-BlackItalic.ttf',
                fontSize = 400,
                fontTagSize = 400,
                ratioWidth = 50,
                ratioHeight = 75,
                targetHeight = None,
                ):
    hashTag = hashTag.upper()
    eachHashTag = hashTag.split(' ')
    # print(eachHashTag)

    # Draw the text first
    fontTag = ImageFont.truetype(fontTagPath,fontTagSize)  
    listTag = []
    listHeight = []
    nameTagWidth = 1000
    for name in eachHashTag:
        tagSize = fontTag.getsize(name)
        tagSize = tagSize[0], tagSize[1]
        canvasTag = Image.new('RGBA', tagSize, 0)
        drawTag = ImageDraw.Draw(canvasTag)
        drawTag.text((0,0), name, font=fontTag, fill=(255,255,255,255))
        currentSize = canvasTag.size
        ratio = nameTagWidth/currentSize[0]
        newSize = int(ratio*currentSize[0]), int(ratio*currentSize[1])
        canvasTag = canvasTag.resize(newSize, Image.ANTIALIAS)
        listTag.append(canvasTag)
        listHeight.append(newSize[1])
        # canvasTag.show()    # Show each tag 
    # print(listTag)
    # print(listHeight, np.sum(listHeight))
    
    pasteWidth = (len(listTag)-1)*20
    pasteHeight = 0
    canvasTagFull = Image.new('RGBA', (nameTagWidth+pasteWidth, np.sum(listHeight)), color=0)
    for tag in listTag:
        canvasTagFull.paste(tag,(pasteWidth,pasteHeight),tag)
        pasteWidth-=20
        pasteHeight+=tag.size[1]
    # canvasTagFull.show()
    # print(canvasTagFull.size)

    # Draw the # sign first
    sign = '#'
    fontSign = ImageFont.truetype(fontPath,fontSize)  
    signSize = fontSign.getsize(sign) 
    canvasHash = Image.new('RGBA', signSize)
    drawSign = ImageDraw.Draw(canvasHash)
    drawSign.text((0,0), sign, font=fontSign, fill=(255,255,255,255))
    #Croping the transparent on top
    canvasHash = canvasHash.crop((0, signSize[1]/5, signSize[0], signSize[1]) )
    H_ratio = canvasTagFull.size[1]/canvasHash.size[1]
    # print(H_ratio,' - ',canvasHash.size[0],' - ', canvasTagFull.size[0])
    H_Size = int(H_ratio*canvasHash.size[0]), int(H_ratio*canvasHash.size[1])
    canvasHash = canvasHash.resize(H_Size, Image.ANTIALIAS)
    # print(canvasHash.size)
    # canvasHash.show()

    #Draw the last paste full size canvas
    canSize = ((canvasTagFull.size[0]+canvasHash.size[0]) , (canvasTagFull.size[1]))
    canvasLastPaste = Image.new('RGBA', (canSize), 0)
    canvasLastPaste.paste(canvasHash,(0,0),canvasHash)
    canvasLastPaste.paste(canvasTagFull,(canvasHash.size[0],0),canvasTagFull)
    # canvasLastPaste.show()
    print('Logo hashtag size = ',canvasLastPaste.size)
    if image!=None:
        L_ratio = (image.size[1]/20)/canvasLastPaste.size[1]
        L_size = int(canvasLastPaste.size[0]*L_ratio), int(canvasLastPaste.size[1]*L_ratio)
        canvasLastPaste = canvasLastPaste.resize(L_size, Image.ANTIALIAS)
        placeH, placeW = (image.size[0]-canvasLastPaste.size[0])*ratioWidth//100, image.size[1]*ratioHeight//100
        image.paste(canvasLastPaste,(placeH, placeW),canvasLastPaste)
        return image
    
    else:
        if targetHeight != None:
            TH_ratio = targetHeight/canvasLastPaste.size[1]
            TH_size = int(TH_ratio*canvasLastPaste.size[0]), int(TH_ratio*canvasLastPaste.size[1])
            canvasLastPaste = canvasLastPaste.resize(TH_size, Image.ANTIALIAS)
            return canvasLastPaste
        else:
            return canvasLastPaste
# drawHashtag()

