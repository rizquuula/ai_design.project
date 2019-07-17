from PIL import ImageFont, ImageDraw, Image, ImageFilter
import cv2 

logoIGPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-instagram.png'
backgroundPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/crop1x1_cv2.jpg'
fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-SemiBoldItalic.ttf'   #Open custom font
fontSize = 400     #Set font size

account_IG = '@rzf.gsh'
account_FB = 'M Razif Rizqullah'
account_WA = '+62 822 3863 9221'
account_LINE = 'r.linkgish'
account_TELEGRAM = None
account_WEB = 'http://www.linkgish.net'
account_TWITTER = 'linkgish'
account_YOUTUBE = 'Razif LinkGish'

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
                    instaAccount=account_IG
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
                        fontSize=50):
    if image==None:
        img = Image.open(backgroundPath)
    else:
        img = image

    canvas = Image.new('RGBA',(img.size[0],img.size[1]//30))
    drawOn = ImageDraw.Draw(canvas)

    logo = Image.open(pathLogo_WA)
    logoH = img.size[1]//30
    logoHratio = logoH/logo.size[1]
    logoNewSize = int(logo.size[0]*logoHratio), int(logo.size[1]*logoHratio)
    logo = logo.resize((logoNewSize), Image.ANTIALIAS)
    logo.show()

    font = ImageFont.truetype(fontPath,fontSize,0,"unic",None)  #Generate font
    textsize = font.getsize(account_WA)   #Getting the width and height of the text
    nameAccCanvas = Image.new('L',textsize)
    drawNAC = ImageDraw.Draw(nameAccCanvas)
    drawNAC.text((0,0), account_WA, font = font, fill = 'white')
    nameAccCanvas.show()

    accountRatio = logoH/textsize[1]
    accountNewSize = int(textsize[0]*accountRatio), int(textsize[1]*accountRatio)

    nameAccCanvas
    
    padding = 10
    accountCanvas = Image.new('RGBA', (accountNewSize[0]+logoNewSize[0]+padding , accountNewSize[1]))
    drawAC = ImageDraw.Draw(accountCanvas)
    

    # canvas.show()
    # img.show()
    
drawAnotherSosmed()