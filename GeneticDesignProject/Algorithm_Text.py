from PIL import ImageFont, ImageDraw, Image, ImageFilter

def TextDrawShade(size=None, font=None, 
                text=None, placex=None, placey=None, 
                fill=None, radius=None):
    # img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example2.jpg",1)
    img_pil = Image.new("RGBA", size,color=0)#fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    textsize = font.getsize(text)   #Getting the width of the text
    # print('Text size = ',textsize)
    margin = 1
    draw.text((placex+margin,placey+margin), text, font = font, fill = fill)
    draw.text((placex+margin,placey-margin), text, font = font, fill = fill)
    draw.text((placex-margin,placey+margin), text, font = font, fill = fill)
    draw.text((placex-margin,placey-margin), text, font = font, fill = fill)
    draw.text((placex,placey), text, font = font, fill =fill) 
    
    result = img_pil.filter(ImageFilter.GaussianBlur(radius=radius))
    return result

def drawTitle(fontPath = None,
                fontSize = None,
                text = None,
                blurRad = 10
                ):
    # fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/IndieFlower/IndieFlower.ttf'   #Open custom font
    # fontSize = 400     #Set font size
    font = ImageFont.truetype(fontPath,fontSize,0,"unic",None)  #Generate font
    # text = "Berubah,-"       #Input title text
    textsize = font.getsize(text)   #Getting the width and height of the text

    canvas = Image.new('RGBA', textsize, 0)
    #Create mask image using other module
    mask_img = TextDrawShade(size=canvas.size,
                font=font,
                text=text,
                placex=0,
                placey=0,
                fill=(0,0,0,255),
                radius=blurRad    
                )
    canvas.paste(mask_img, (0,0), mask=None)
    draw = ImageDraw.Draw(canvas)
    draw.text((0,0), text, font = font, fill = 'white')
    # canvas.show()
    return canvas
    # mask_img.show()
    # print(overlay_img.size, img_crop.size, mask_img.size) #Checking, all should be same

    #Draw the image again for create Title Text

'''drawTitle(fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/IndieFlower/IndieFlower.ttf',
    fontSize = 400,
    text = "Berubah,-",
    ).show()'''