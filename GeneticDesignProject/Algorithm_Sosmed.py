from PIL import ImageFont, ImageDraw, Image, ImageFilter
import cv2 

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

def drawIGaccount(logo=logoIGPath,
                    backgroundPath=backgroundPath,
                    backgroundImg=None,
                    fontPath=fontPath,
                    fontSize=fontSize,
                    instaAccount='@Rzf.Gsh'
                    ):

    logoIG = Image.open(logo)
    if backgroundImg==None:
        openImg = Image.open(background)
    else:
        openImg = backgroundImg

    OverlayColor = Image.new('L',logoIG.size,'white')
    logoIG_white = Image.composite(OverlayColor, logoIG, logoIG)

    font = ImageFont.truetype(fontPath,fontSize,0,"unic",None)  #Generate font
        #Input title text
    textsize = font.getsize(instaAccount)   #Getting the width and height of the text
    # print(textsize) 
    # print(logoIG.size) 

    ratio = logoIG.size[1]/textsize[1] #Ratio
    newTextSize = int(textsize[0]*ratio), int(textsize[1]*ratio)

    newFrameSize = newTextSize[0], logoIG.size[0]*2
    # print(ratio)

    textArea = Image.new('L',textsize,color=0)
    drawText = ImageDraw.Draw(textArea)
    drawText.text((0,0), instaAccount, font = font, fill = 'white')
    # textArea.show()
    textArea = textArea.resize((newTextSize), Image.ANTIALIAS)
    # print(textArea.size)

    newFrame = Image.new('L',newFrameSize,color=0)
    newFrame.paste(logoIG_white, (newFrameSize[0]//2-logoIG_white.size[0]//2, 0), logoIG_white)
    newFrame.paste(textArea, (0, textArea.size[1]), textArea)

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

def drawAnotherSosmed(isTrue=False,
                        image=None,
                        backgroundPath=backgroundPath,
                        fontPath=fontPath,
                        fontSize=fontSize,
                        heightFactor = 50,
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
    logoH = img.size[1]//heightFactor
    # What logo will be create next? Make a list first
    listLogoPath = [pathLogo_FB, 
                        pathLogo_LINE, pathLogo_TELEGRAM, 
                        pathLogo_TWITTER, pathLogo_WA, 
                        pathLogo_WEB, pathLogo_YOUTUBE]
    listAccount = [account_FB,
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