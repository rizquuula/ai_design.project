from PIL import Image, ImageFilter, ImageDraw

def dropShadow(image, imageSize=(0,0), imagePlace=(0,0),
                offset=(5,5), border=20,
                background=0xffffff, shadow=0x444444, 
                iterations=1):
    #Just for image
    #Fail to test in text
    #Create background image
    #Drop Shadow
    expandX = abs(offset[0]) + 2*border
    expandY = abs(offset[1]) + 2*border
    newX, newY = (imageSize[0] + expandX) , (imageSize[1] + expandY)
    imageBack = Image.new(image.mode, (newX,newY), background)
    
    #Place the shadow
    shadowLeft = imagePlace[0] + max(offset[0],0)
    shadowTop = imagePlace[1] + max(offset[1],0) 
    imageBack.paste(shadow, [shadowLeft, shadowTop, shadowLeft + imageSize[0], 
    shadowTop + imageSize[1]] )
    
    #Make iteration for blurry
    x = 0
    while x<iterations:
        imageBack = imageBack.filter(ImageFilter.BLUR)
        x+=1

    # # Paste the input image onto the shadow backdrop  
    # imageLeft =  imagePlace[0] - min(offset[0], 0)
    # imageTop =  imagePlace[1] - min(offset[1], 0)
    # imageBack.paste(image, (imageLeft, imageTop))
    
    return imageBack

def textShadow(imgSource,text,place,offset,font,fillcolor,shadowcolor):
    draw = ImageDraw.Draw(imgSource)
    # font = ImageFont.truetype(font, pointsize)
    x,y = place[0], place[1] 

    # thin border
    draw.text((x-offset, y), text, font=font, fill=shadowcolor)
    draw.text((x+offset, y), text, font=font, fill=shadowcolor)
    draw.text((x, y-offset), text, font=font, fill=shadowcolor)
    draw.text((x, y+offset), text, font=font, fill=shadowcolor)

    # thicker border
    draw.text((x-offset, y-offset), text, font=font, fill=shadowcolor)
    draw.text((x+offset, y-offset), text, font=font, fill=shadowcolor)
    draw.text((x-offset, y+offset), text, font=font, fill=shadowcolor)
    draw.text((x+offset, y+offset), text, font=font, fill=shadowcolor)

    # now draw the text over it
    draw.text((x, y), text, font=font, fill=fillcolor)
    n = 0
    while n < 5:
        draw = draw.filter(ImageFilter.BLUR)
        n += 1
    return draw 

# from wand.color import Color
# from wand.compat import nested
# from wand.drawing import Drawing
# from wand.image import Image
# import wand.display
# import cv2

from wand.color import Color
from wand.compat import nested
from wand.drawing import Drawing
from wand.image import Image
import numpy as np
import wand.display
def textShadowWand(image=None, filePath=None, fontSize=None, place=None, 
                    inputText=None, blur = (10,5),
                    fillcolor=None,shadowcolor=(0,0,0,0.5),
                    traceback=None):
    dimensions = {'width': image[0],
                'height': image[1]}
    print(dimensions)
    with nested(Image(filename=(filePath), **dimensions),
            Image(background=Color('transparent'), **dimensions)) as (bg, shadow):
        # Draw the drop shadow
        with Drawing() as ctx:
            ctx.font = 'Candice'
            ctx.push()
            thecolor = str('rgba'+str(shadowcolor))
            print('thecolor : ',thecolor)
            # str('rgba'+(3, 3, 3, 1))
            ctx.fill_color = Color(thecolor)
            # ctx.fill_color = Color('rgba(0,0,0,0.33)')
            ctx.font_size = fontSize
            ctx.text(place[0], place[1], inputText)
            print(place[0], place[1], inputText)
            print('ctx is ',ctx)
            ctx(shadow)
        # Apply filter
        # print(np.array(shadow.shape))
        
        shadow.gaussian_blur(7, 4)
        # Draw text
        with Drawing() as ctx:
            thecolor = str('rgba'+str(fillcolor))
            print('thecolor : ',thecolor)
            ctx.fill_color = Color(thecolor)
            ctx.font_size = fontSize
            ctx.text(place[0], place[1], inputText)
            print(place[0], place[1], 'LinkGish')
            ctx(shadow)
        bg.composite(shadow, 0, 0)
        traceback = str(traceback)
        bg.save(filename='/home/linkgish/Desktop/WebApp2/GeneticDesignProject/OutputWand.png')
        #wand.display.display(bg)

    return bg 


