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
