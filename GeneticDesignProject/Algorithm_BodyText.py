import cv2
import numpy as np 
from PIL import ImageFont, ImageDraw, Image, ImageFilter
import textwrap

def MakeBodyText(size=None, text=None, 
                    FONT_PATH=None, FONT_SIZE=None, 
                    wrap_width=40, padding=10,
                    rect_fill=(255,255,255,210),
                    font_color=(0,0,0,255),
                    isBackRect=False,
                    blurRectRadius=15,
                    image=None,
                    ):
    # img = Image.new("RGBA", size, 0)
    
    # img = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/crop1x1_cv2.jpg')
    # original_img = img 
    # text = 'Bukanlah kesabaran jika masih mempunyai batas dan bukanlah keikhlasan jika masih merasakan sakit.'
    # FONT_PATH = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/IndieFlower.ttf'   #Open custom font
    # FONT_SIZE = 20     #Set font size
    font = ImageFont.truetype(FONT_PATH,FONT_SIZE)  #Generate font
    text_size = font.getsize(text)
    print('text size = ',text_size)
    
    wrapped = textwrap.wrap(text,width=wrap_width)
    
    widthBox = []
    for text in wrapped:
        # lenWrapped.append(len(text))
        print(text)
        widthText = font.getsize(text)
        widthBox.append(widthText)
    # longestStr = wrapped[np.argmax(lenWrapped)]
    # print(longestStr)
    widthLongestStr = np.max(widthBox)
    print('widthLongestStr = ', widthLongestStr)
    img = Image.new("RGBA", (widthLongestStr,text_size[1]*len(wrapped)), 0)
    draw = ImageDraw.Draw(img,'RGBA')
    img_size = img.size
    print('img size = ',img_size)
    current_h= 0# img_size[0]//3
    if isBackRect == True:
        rect = Image.new("RGBA", img.size, color=0)
        drawRect = ImageDraw.Draw(rect)

        width_box = []
        height_box = []

        for line in wrapped:
            w,h = draw.textsize(line,font=font)
            width_box.append(w)
            height_box.append(h)
        print('box w,h = ', width_box, 'and ',height_box)
        
        drawRect.rectangle((((img_size[0]-max(width_box))//2-padding, current_h-padding), 
                        ((img_size[0]-max(width_box))//2+padding+max(width_box), 
                            padding*2+current_h+sum(height_box))), 
                        fill=rect_fill)

        rect_result = rect.filter(ImageFilter.GaussianBlur(radius=blurRectRadius))
        # print(rect_result.size,original_img.size)
        img.paste(rect_result,(0,0),rect_result)
    
    elif isBackRect==False:
        pass
    # draw = ImageDraw.Draw(result,'RGBA')
    counter = 0
    for line in wrapped:
        w, h = draw.textsize(line,font=font)
        # print('w,h = ',w,'and ',h)
        # print('line ', line)
        # draw.rectangle((((img_size[0]-w)//2, current_h), (w,h)), fill='white')
        draw.text(((img_size[0]-w)//2, current_h), line, font=font, fill=font_color)
        current_h+=h
        counter+=1
    # img2.show()
    print('current_h = ',current_h)
    # draw.text((img_size[0]-130,(img_size[1]*14//15)),'Created by AiDesign',fill='white',font=subs_font)
    '''
    current_h = img_size[0]//2
    for line in wrapped:
        w, h = draw.textsize(line,font=font)
        # print('w,h = ',w,'and ',h)
        # print('line ', line)
        # draw.rectangle((((img_size[0]-w)//2, current_h), (w,h)), fill='white')
        draw.text(((img_size[0]-w)//2+1, current_h+6), line, font=font, fill=(0,0,0,1))
        current_h+=h
        # draw.text((0,0), text, font = font, fill = (0,0,0,1))
        '''
    # print(draw.getsize)

    # img.show()
    
    return img, counter 
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
