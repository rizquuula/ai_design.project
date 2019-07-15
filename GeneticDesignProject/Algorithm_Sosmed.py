from PIL import ImageFont, ImageDraw, Image, ImageFilter

DevAccountTeehee = "@Rzf.Gsh"
logoIGPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-instagram.png'
backgroundPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/ResultImage.jpg'
fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-SemiBoldItalic.ttf'   #Open custom font
fontSize = 400     #Set font size

def drawIGaccount(logo=logoIGPath,
                    backgroundPath=backgroundPath,
                    backgroundImg=None,
                    fontPath=fontPath,
                    fontSize=fontSize,
                    instaAccount=DevAccountTeehee
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