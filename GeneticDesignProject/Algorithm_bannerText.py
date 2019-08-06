from PIL import Image, ImageDraw, ImageFont, ImageFilter
from Algorithm_BackgroundManipulation import imgResizer
from Algorithm_PIL_cv2 import PILtoCV2

import numpy as np 
import textwrap


def drawBannerTitle(fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Comfortaa/Comfortaa-Bold.ttf',
                fontSize = 300,
                text = 'this is example of banner title text',
                # maxWidth = 500,
                # maxHeight = 500,
                image = None,
                ratioWidth = 30,
                ratioHeight = 10,
                pasteXratio = 20,
                pasteYratio = 60,
                percentTransparency = 100,
                fontColor = None,
                ):
    print()
    maxWidth = int((ratioWidth/100)*image.size[0])
    maxHeight = int((ratioHeight/100)*image.size[1])
    print('maxWidth,maxHeight = ',maxWidth,maxHeight)

    pasteX = int((pasteXratio/100)*image.size[0])
    pasteY = int((pasteYratio/100)*image.size[1])
    print(pasteX,pasteY)

    fontstyle = ImageFont.truetype(font=fontPath,
                                size=fontSize)
    text = text.upper()
    textWrapped = textwrap.wrap(text, 
                            width=int((len(text))*0.6),
                            # width=int((len(text))*0.4),
                            )
    # wordCount = 0
    # for word in text.split(' '):
    #     wordCount+=(len(word))

    # # middle
    # print(wordCount)
    totalH = 0
    textWBox = []
    textPIL = []
    # imageCv2 = image # PILtoCV2(image=image)
    
    # if (len(fontColor))==3:
    #     fontColor = (fontColor)+(alphaChannel,)
    print('fontColor = ',fontColor)
    for t in textWrapped: # text.split(' '):
        textSize = fontstyle.getsize(t)

        textImage = Image.new('RGBA', textSize, color=0)
        drawEachText = ImageDraw.Draw(textImage,'RGBA')
        drawEachText.text((0,0),
                        t,
                        font=fontstyle,
                        fill= fontColor
                        )
        # Resizing 
        textImage =  imgResizer(img=textImage,
                                    # targetHeight=maxHeight,
                                    targetWidth=maxWidth,
                                    )

        textPIL.append(textImage)
        textWBox.append(textImage.size[0])
        totalH+=textImage.size[1]

    print('textPIL = ',textPIL)
    print('textWBox = ',textWBox)
    canvas = Image.new('RGBA',(np.max(textWBox), totalH),0)
    
    currentH = 0
    for i in textPIL:
        canvas.paste(i,(0,currentH))
        currentH+=i.size[1]

    # canvas.show()
    # for i in textPIL:
    #     i.show()

    if canvas.size[0]>maxWidth:
        print('the title text need to be resize first.. resizing apply..')
        canvas = imgResizer(img=canvas,
                        targetWidth=maxWidth)
    if canvas.size[1]>maxHeight:
        print('the title text need to be resize again.. resizing apply..')
        canvas = imgResizer(img=canvas,
                        targetHeight=maxHeight)

    pasteY = int(pasteY-(0.5*canvas.size[1]))
    # mask = Image.new('RGBA',canvas.size,color=(255,255,255,100))
    paste_mask = canvas.split()[3].point(lambda i: i * percentTransparency / 100.)
    # paste_mask.show()
    image.paste(canvas,(pasteX,pasteY),mask=paste_mask)
    return image

def drawBannerDetail(image = None,
                logoH = 100,
                fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Comfortaa/Comfortaa-Bold.ttf',
                fontSize = 100,
                placeText = 'Write here, place the event held',
                dateText = 'Day, dd mm yyyy',
                timeText = 'time aa.mm - pp.mm zone',
                textPadding = 70,
                ratioXpaste = 60,
                ratioYpaste = 50,
                ratioXsize = 30,
                ):
    print()
    pasteX = int((ratioXpaste/100)*image.size[0])
    pasteY = int((ratioYpaste/100)*image.size[1])
    # Import logo-logo
    placeLogo = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Object-lib/loct-new.png')
    # placeLogo = imgResizer(img=placeLogo,
    #                 # targetHeight=image.size[1]//10,
    #                 targetHeight= logoH,
    #                 )
    dateLogo = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Object-lib/calendar-new.png')
    # dateLogo = imgResizer(img=dateLogo,
    #                 # targetHeight=image.size[1]//10,
    #                 targetHeight= logoH,
    #                 )
    timeLogo = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Object-lib/time-new.png')
    # timeLogo = imgResizer(img=timeLogo,
    #                 # targetHeight=image.size[1]//10,
    #                 targetHeight= logoH,
    #                 )
    # Make it in a list for iteration process
    listLogo = [dateLogo, timeLogo, placeLogo]
    # Some necessary situation
    # longestDetail = np.max([len(dateText), len(timeText)])  # Place detail will follow the longest detail here
    if (len(placeText) > 2*len(dateText)) or (len(placeText) > 2*len(timeText)):
        print('active wrap type 1')
        placeTextWrapped = textwrap.wrap(placeText, 
                                        # width=longestDetail+10,
                                        width=int(len(placeText)*0.35),
                                        ) # Wrap the place detail 
        numberLine = 2 + len(placeTextWrapped)

    elif (len(placeText) > len(dateText)) or (len(placeText) > len(timeText)):
        print('active wrap type 2')
        placeTextWrapped = textwrap.wrap(placeText, 
                                        # width=longestDetail+10,
                                        width=int(len(placeText)*0.55),
                                        ) # Wrap the place detail 
        numberLine = 2 + len(placeTextWrapped)

    else:
        print('active no wrap')
        placeTextWrapped = placeText
        numberLine = 3
    # Determine max logo width 
    logoWidth = []
    logoHeight = []
    for logo in listLogo:
        logoWidth.append(logo.size[0])
        logoHeight.append(logo.size[1])
    logoWidthMax = np.max(logoWidth)
    # Draw logo and text in a loop 
    logoWithText = []
    fontStyle = ImageFont.truetype(font= fontPath,
                                size= fontSize,
                                )
    listText = [dateText, timeText, placeTextWrapped]
    dateTextSize = fontStyle.getsize(dateText)
    # numberLine = 2 + len(placeTextWrapped)
    # Determine text canvas size
    totalTextHeight = dateTextSize[1]*numberLine + 2*textPadding
    p_x = []
    for p in placeTextWrapped:
        p_w = fontStyle.getsize(p)[0]
        p_x.append(p_w)
    p_x.append(fontStyle.getsize(dateText)[0])
    p_x.append(fontStyle.getsize(timeText)[0])
    totalTextWidth = np.max(p_x)
    textCanvas = Image.new('RGBA', (totalTextWidth, totalTextHeight), 0)
    drawText = ImageDraw.Draw(textCanvas)
    Y = 0
    T_H = []
    for text in listText:
        if (isinstance(text, list)) == True:
            # subY = Y
            for t in text:
                subTextSize = fontStyle.getsize(t)
                drawText.text((0,Y),
                t,
                fill='white',
                font=fontStyle)
                # subY+=subTextSize[1]
                Y+=subTextSize[1]
        else: 
            textSize = fontStyle.getsize(text)
            drawText.text((0,Y),
                text,
                fill='white',
                font=fontStyle)
            Y+=textSize[1]+textPadding
            T_H.append(textSize[1])
    # textCanvas = imgResizer(img=textCanvas,
    #                 targetHeight=300)
    # textCanvas.show()
    # Draw text detail done here
    # Start to draw the logo 
    # logoWidthMax = logoWidthMax      # Declared on top
    L_H = np.max(T_H)  # Max text size is set as default logo height 

    logoHeightMax = L_H*3 + textPadding*2  # WIll be full logo height
    logoCanvas = Image.new('RGBA',(L_H, logoHeightMax),0)
    L_Y = 0
    # count = 0
    for logo in listLogo:
        logo = imgResizer(img=logo, 
                        targetHeight=L_H)
        logoCanvas.paste(logo,(0,L_Y),logo)
        L_Y+=L_H+textPadding
        # count+=1
    # logoCanvas.show()
    textPadding = textPadding//4
    textLogoCanvasSize = textCanvas.size[0]+logoCanvas.size[0]+textPadding, np.max([textCanvas.size[1], logoCanvas.size[1]])
    textLogoCanvas = Image.new('RGBA', textLogoCanvasSize, 0)
    textLogoCanvas.paste(logoCanvas,(0,0),logoCanvas)
    textLogoCanvas.paste(textCanvas,(logoCanvas.size[0]+textPadding, textPadding//3),textCanvas)

    ratioXsize = int(image.size[0]*(ratioXsize/100))

    textLogoCanvas = imgResizer(img=textLogoCanvas, 
                            targetWidth=ratioXsize)
    # textLogoCanvas.show()

    # Paste the result to the background image 
    pasteY = int(pasteY-(0.5*textLogoCanvas.size[1]))
    pastePotitions = pasteX, pasteY
    image.paste(textLogoCanvas, pastePotitions, textLogoCanvas)

    return image

# drawBannerDetail()