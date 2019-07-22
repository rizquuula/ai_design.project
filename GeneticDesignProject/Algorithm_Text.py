from PIL import ImageFont, ImageDraw, Image, ImageFilter

def TextDrawShade(size=None, font=None, image=None,
                text=None, placex=None, placey=None, 
                fill=None, radius=None, margin=5):
    if image==None:
        # img = cv2.imread("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example2.jpg",1)
        img_pil = Image.new("RGBA", size,color=0)#fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        textsize = font.getsize(text)   #Getting the width of the text
        # print('Text size = ',textsize)
        # margin = 1
        draw.text((placex+margin,placey+margin), text, font = font, fill = fill)
        draw.text((placex+margin,placey-margin), text, font = font, fill = fill)
        draw.text((placex-margin,placey+margin), text, font = font, fill = fill)
        draw.text((placex-margin,placey-margin), text, font = font, fill = fill)
        draw.text((placex,placey), text, font = font, fill =fill) 
        
        result = img_pil.filter(ImageFilter.GaussianBlur(radius=radius))
        return result
    else:
        # margin = margin 
        imageSize = image.size[0]+(2*margin), image.size[1]+(2*margin)

        img = Image.new('RGBA', imageSize, 0)
        mask = Image.new('L', imageSize, color='black')
        img.paste(image, (0,margin), image)
        img.paste(image, (margin,0), image)
        img.paste(image, (2*margin,margin), image)
        img.paste(image, (margin,2*margin), image)
        img = Image.composite(mask, img, img)
        # img.show()
        result = img.filter(ImageFilter.GaussianBlur(radius=radius))
        result.paste(image,(margin,margin), image)
        return result

def drawTitle(fontPath = None,
                fontSize = None,
                image = None,
                text = None,
                blurRad = 10,
                shadowColor = (0,0,0,255),
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
                fill=shadowColor,
                radius=blurRad    
                )
    canvas.paste(mask_img, (0,0), mask=None)
    draw = ImageDraw.Draw(canvas)
    draw.text((0,0), text, font = font, fill = 'white')

    ratio = (image.size[0]/2)/canvas.size[0]
    canvas = canvas.resize((int(canvas.size[0]*ratio), int(canvas.size[1]*ratio)) ,Image.ANTIALIAS)
    # canvas.show()
    image.paste(canvas,((image.size[0]-canvas.size[0])//2, image.size[1]//4),canvas)
    # canvas.show()
    return image, canvas
    # mask_img.show()
    # print(overlay_img.size, img_crop.size, mask_img.size) #Checking, all should be same

    #Draw the image again for create Title Text

# drawTitle(fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/IndieFlower/IndieFlower.ttf',
#     fontSize = 400,
#     text = "Berubah,-",
#     ).show()