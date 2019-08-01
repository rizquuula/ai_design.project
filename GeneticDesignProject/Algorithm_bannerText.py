from PIL import Image, ImageDraw, ImageFont, ImageFilter
from Algorithm_logoMaker import imgResizer
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