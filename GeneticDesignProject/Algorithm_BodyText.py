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
                    ):
    img = Image.new("RGBA", size, color=(0,0,0,0))
    # img = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/crop1x1_cv2.jpg')
    # original_img = img 
    # text = 'Bukanlah kesabaran jika masih mempunyai batas dan bukanlah keikhlasan jika masih merasakan sakit.'
    # FONT_PATH = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/IndieFlower.ttf'   #Open custom font
    # FONT_SIZE = 20     #Set font size
    font = ImageFont.truetype(FONT_PATH,FONT_SIZE)  #Generate font
    subs_font = ImageFont.truetype(FONT_PATH,FONT_SIZE//2)
    text_size = font.getsize(text)
    img_size = img.size
    print('text size = ',text_size)
    print('img size = ',img_size)
    wrapped = textwrap.wrap(text,width=wrap_width)

    draw = ImageDraw.Draw(img,'RGBA')
    current_h= img_size[0]//3
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
        print(rect_result.size,original_img.size)
        img.paste(rect_result,(0,0),rect_result)
    
    elif isBackRect==False:
        pass
    # draw = ImageDraw.Draw(result,'RGBA')
    for line in wrapped:
        w, h = draw.textsize(line,font=font)
        # print('w,h = ',w,'and ',h)
        # print('line ', line)
        # draw.rectangle((((img_size[0]-w)//2, current_h), (w,h)), fill='white')
        draw.text(((img_size[0]-w)//2, current_h+5), line, font=font, fill=font_color)
        current_h+=h
    # img2.show()
    draw.text((img_size[0]-130,(img_size[1]-20)),'Created by AiDesign',fill='white',font=subs_font)
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
    return img 
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
