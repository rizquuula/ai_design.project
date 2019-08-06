import cv2
import numpy as np 
import random
from PIL import ImageFont, ImageDraw, Image, ImageFilter
import textwrap
from Algorithm_colorMaterial import randomMaterialColor, LIGHTorDARK
from Algorithm_BackgroundManipulation import imgResizer

def MakeBodyText(image=None, text=None, 
                    FONT_PATH=None, FONT_SIZE=None, 
                    wrap_width=40, padding=10,
                    rect_fill=(255,255,255,210),
                    # font_color=(0,0,0,255),
                    isBackRect=False,
                    blurRectRadius=15,
                    textXratio = 50,
                    textYratio = 50,
                    placeYRatio = 50,
                    ):
    font = ImageFont.truetype(FONT_PATH,FONT_SIZE)  #Generate font
    text_size = font.getsize(text)
    print('text size = ',text_size)
    
    wrapped = textwrap.wrap(text,width=wrap_width)    # Wrapping text based on total char as width
    
    widthBox = []   # Collect width each word
    for text in wrapped:
        # lenWrapped.append(len(text))
        print(text) # Print the text that wrapped per line
        widthText = font.getsize(text)      # Get size of each line
        widthBox.append(widthText)  #
    # longestStr = wrapped[np.argmax(lenWrapped)]
    # print(longestStr)
    widthLongestStr = np.max(widthBox)
    print('widthLongestStr = ', widthLongestStr)
    canvasSize = widthLongestStr,text_size[1]*len(wrapped)
    print('canvasSize = ', canvasSize)
    canvas = Image.new("RGBA", (canvasSize), 0)
    
    maxtextXsize = int((textXratio/100)*image.size[0])
    maxtextYsize = int((textYratio/100)*image.size[1])
    
    print('maxtextsize = ',maxtextXsize,maxtextYsize)

    cnvImgRatio = maxtextXsize/canvas.size[0]
    # print('cnvImgRatio = ', cnvImgRatio)
    # print('Canvas by ratio = ', cnvImgRatio*canvas.size[0], cnvImgRatio*canvas.size[1])

    pasteX = int((image.size[0]-(canvas.size[0]*cnvImgRatio))/2)
    # print('Paste X = ',image.size[0],(canvas.size[0]*cnvImgRatio))
    
    # pasteY = (image.size[1]//4)+(image.size[1]//30) # + titleDraw.size[1]
    pasteY = int((placeYRatio/100)*image.size[1])
    # maxtextYsize = int(textYratio/100)*image.size[1]
    # print('sizeX, sizeY = ',int(widthLongestStr*cnvImgRatio), maxtextYsize)

    autoColor = LIGHTorDARK(image=image,
                        posX=pasteX,
                        posY=pasteY,
                        sizeX=maxtextXsize,
                        sizeY=maxtextYsize
                        )


    draw = ImageDraw.Draw(canvas,'RGBA')
    # canvas.size = canvas.size
    print('canvas size = ',canvas.size)
    current_h= 0# canvas.size[0]//3
    if isBackRect == True:
        rect = Image.new("RGBA", canvas.size, color=0)
        drawRect = ImageDraw.Draw(rect)

        width_box = []
        height_box = []

        for line in wrapped:
            w,h = draw.textsize(line,font=font)
            width_box.append(w)
            height_box.append(h)
        print('box w,h = ', width_box, 'and ',height_box)
        
        drawRect.rectangle((((canvas.size[0]-max(width_box))//2-padding, current_h-padding), 
                        ((canvas.size[0]-max(width_box))//2+padding+max(width_box), 
                            padding*2+current_h+sum(height_box))), 
                        fill=rect_fill)

        rect_result = rect.filter(ImageFilter.GaussianBlur(radius=blurRectRadius))
        # print(rect_result.size,original_canvas.size)
        canvas.paste(rect_result,(0,0),rect_result)
    
    elif isBackRect==False:
        pass
    # draw = ImageDraw.Draw(result,'RGBA')
    counter = 0
    for line in wrapped:
        w, h = draw.textsize(line,font=font)
        # print('w,h = ',w,'and ',h)
        # print('line ', line)
        # draw.rectangle((((canvas.size[0]-w)//2, current_h), (w,h)), fill='white')
        draw.text(((canvas.size[0]-w)//2, current_h), line, font=font, fill=autoColor)
        current_h+=h
        counter+=1
    # canvas2.show()
    print('current_h = ',current_h)
    textYsize = (image.size[1]//20) * counter
    # maxtextYsize = (textXratio/100)*image.size[1]
    
    if textYsize>maxtextYsize:      # If text too long so it reached the maximul height available
        print('Using textYsize > maxtextYsize statement')
        ratioBodyText = maxtextYsize/canvas.size[1]
        newBodyTextSize = int(canvas.size[0]*ratioBodyText), int(canvas.size[1]*ratioBodyText)
        canvas = canvas.resize(newBodyTextSize, Image.ANTIALIAS)

    else: # For short text
        print(textYsize,' from ', counter, ' multiple by ', (image.size[1]//20))
        ratioBodyText = textYsize/canvas.size[1]
        newBodyTextSize = int(canvas.size[0]*ratioBodyText), int(canvas.size[1]*ratioBodyText)
        canvas = canvas.resize(newBodyTextSize, Image.ANTIALIAS)
    
    textXsize = canvas.size[0]
    if textXsize>maxtextXsize:
        ratioXbody = maxtextXsize/canvas.size[0]
        newBodyTextSize = int(canvas.size[0]*ratioXbody), int(canvas.size[1]*ratioXbody)
        canvas = canvas.resize(newBodyTextSize, Image.ANTIALIAS)
    else: 
        pass

    print('Last canvas size = ', canvas.size)
    pasteX = int((image.size[0]-newBodyTextSize[0])/2)
    image.paste(canvas,(int(pasteX),int(pasteY)),canvas)
    # return canvas, counter 
    return image
    # cv2.waitKey(0)

# MakeBodyText(size=(600,600), 
#                     text='Bukanlah kesabaran jika masih mempunyai batas dan bukanlah keikhlasan jika masih merasakan sakit.', 
#                     FONT_PATH='/home/linkgish/Desktop/WebApp2/GeneticDesignProject/IndieFlower.ttf',   #Open custom font, 
#                     FONT_SIZE=20, 
#                     wrap_width=40, 
#                     padding=10,
#                     rect_fill=(255,255,255,180),
#                     font_color=(255,255,255,255),
#                     isBackRect=False,
#                     blurRectRadius=15,
#                     ).show()

fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-BlackItalic.ttf'   #Open custom font
def makeBodyTextNano2(image = None,
            fontPath = fontPath, 
            fontSize = 20,
            text = 'Ketika kamu mulai memahami suatu hal. Teruslah memahami hingga kau paham bahwa dirimu sama sekali belum paham hal tersebut.',
            wrapWidth = 30,
            placeXRatio = None,
            placeYRatio = None,
            fieldXRatio = 50,
            fieldYRatio = 70,
            # typeColor = 'light',
            ):
    font = ImageFont.truetype(fontPath, fontSize)
    textSize = font.getsize(text)

    wrapped = textwrap.wrap(text,width=wrapWidth)
    print('Wrapped result : ', wrapped)
    
    widthBox = []
    heightBox = []
    for texts in wrapped:
        print(texts)
        sizeText = font.getsize(texts)
        widthBox.append(sizeText[0])
        heightBox.append(sizeText[1])
    # print('widthBox : ',widthBox)
    textMaxWidth = np.max(widthBox)
    textMaxHeight = np.max(heightBox)
    
    textFieldsize = textMaxWidth, np.sum(heightBox) # +300, np.sum(heightBox)
    textField = Image.new('RGBA', textFieldsize, 0)
    draw = ImageDraw.Draw(textField, 'RGBA')

    fieldHRatio = ((fieldYRatio/100 )*image.size[1])/textField.size[1]
    
    #Set paste potition
    placeXRatio = placeXRatio/100
    placeYRatio = placeYRatio/100
    posX = int(image.size[0]*placeXRatio)
    posY = int(image.size[0]*placeYRatio)

    startX = 0 # +random.randint(0,300)
    startY = 0
    for texts in wrapped:
        words = texts.split(" ")
        # print(words)
        for word in words:
            word = str(word+' ')
            
            whatsColoris = LIGHTorDARK(image=image,
                        posX=posX + int(startX*fieldHRatio),
                        posY=posY + int(startY*fieldHRatio),
                        sizeX=int((font.getsize(word)[0]) * fieldHRatio),
                        sizeY=int((font.getsize(word)[1]) * fieldHRatio)
                        )
            print(posX, posY, startX, startY, font.getsize(word),fieldHRatio)

            print('word : ', word, 'Typecolor used is : ', whatsColoris)
            randomColor = randomMaterialColor(typeColor=whatsColoris) 
            draw.text((startX,startY), word , fill= randomColor, font= font)
            startX+=(font.getsize(word))[0]
            print()
        startY+=(font.getsize(texts))[1]
        startX = 0 # +random.randint(0,300)
    # print('draw text pass')
    # textField.show()
    # fieldHRatio = ((fieldYRatio/100 )*image.size[1])/textField.size[1]
    print('fieldYRatio = ',fieldHRatio)
    textField = textField.resize((int(textField.size[0]*fieldHRatio),int(textField.size[1]*fieldHRatio)), Image.ANTIALIAS)

    
    fieldMaxWidth = (fieldXRatio/100 )*image.size[0]
    if textField.size[0] > fieldMaxWidth:
        fieldWRatio = fieldMaxWidth/textField.size[0]    
        textField = textField.resize((int(textField.size[0]*fieldWRatio),int(textField.size[1]*fieldWRatio)), Image.ANTIALIAS)
        
        image.paste(textField,(posX, posY),textField)
        return image
    else: 
        # textField.show()
        image.paste(textField,(posX, posY),textField)
        return image

# drawBodyText()

def drawRectangularText(text = 'Semoga umat manusia berbahagia',
                    image = Image.new('RGBA', (500,500), color='grey'),
                    fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Muli/Muli-BlackItalic.ttf',   #Open custom font
                    fontSize = 200,
                    padding = 10,
                    ):
    # print('as')
    sideSize = image.size[0]//8
    centerSize = image.size[0]//2
    canvas = Image.new('RGBA', (image.size), 0)
    font = ImageFont.truetype(fontPath, fontSize)

    draw = ImageDraw.Draw(canvas)
    draw.rectangle(((centerSize-sideSize, centerSize-sideSize), (centerSize+sideSize, centerSize+sideSize)), 
                fill = 'red')

    count = 0
    
    centerX = centerSize
    centerY = centerSize
    pos1X, pos1Y = 0, 0
    pos2X, pos2Y = 0, 0
    pos3X, pos3Y = 0, 0
    pos4X, pos4Y = 0, 0

    offsetYpos1, offsetYpos2, offsetYpos3, offsetYpos4 = 0, 0, 0, 0
    # print('placeX, placeY = ', placeX, placeY)
    text = text.split()
    for word in text:
        word = word.upper()
        wordSize = font.getsize(word)
        count+=1

        textCanvas = Image.new('RGBA', wordSize, 0)
        drawText = ImageDraw.Draw(textCanvas)
        drawText.text((0,0), word, fill = 'white', font=font )
        textWidth = int(sideSize*2.5)
        textCanvas = imgResizer(img=textCanvas,
                        targetWidth=textWidth)
        
        if count%4 == 1:
            print('POTITION 1 :: ', word)
            # print('wordSize, target W, resized = ', wordSize, textWidth, textCanvas.size)
            pos1X = centerX - sideSize
            pos1Y = centerY - sideSize - textCanvas.size[1] - padding
            print('Paste Location = ', pos1X, pos1Y)
            canvas.paste(textCanvas,(pos1X, pos1Y ),textCanvas)
            pos1Y += textCanvas.size[1] + padding
            offsetYpos1 = textCanvas.size[0] - sideSize*2
        
        elif count%4 == 2:
            print('POTITION 2 :: ',word)
            textCanvas = imgResizer(img = textCanvas,
                                targetHeight = offsetYpos1)
            textCanvas = textCanvas.rotate(-90, expand = 1)

            pos2X = centerSize + sideSize + padding
            pos2Y = centerSize - sideSize
            print('Paste Location = ', pos2X, pos2Y)
            canvas.paste(textCanvas,(pos2X, pos2Y ),textCanvas)
            pos2X += textCanvas.size[0] + padding
        elif count%4 == 3:
            pass
        elif count%4 == 0:
            pass

    return canvas
drawRectangularText().show()