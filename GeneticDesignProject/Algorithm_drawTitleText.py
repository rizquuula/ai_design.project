from PIL import ImageFont, ImageDraw, Image, ImageFilter
from Algorithm_Text import TextDrawShade

FONT_PATH = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/IndieFlower/IndieFlower.ttf'   #Open custom font
FONT_SIZE = 400     #Set font size
font = ImageFont.truetype(FONT_PATH,FONT_SIZE,0,"unic",None)  #Generate font
TITLE_TEXT = "Berubah,-"       #Input title text
textsize = font.getsize(TITLE_TEXT)   #Getting the width and height of the text

canvas = Image.new('RGBA', textsize, 0)
#Create mask image using other module
mask_img = TextDrawShade(size=canvas.size,
            font=font,
            text=TITLE_TEXT,
            placex=0,
            placey=0,
            fill=(0,0,0,200),
            radius=10    
            )
canvas.paste(mask_img, (0,0), mask=None)
draw = ImageDraw.Draw(canvas)
draw.text((0,0), TITLE_TEXT, font = font, fill = 'white')
canvas.show()
# mask_img.show()
# print(overlay_img.size, img_crop.size, mask_img.size) #Checking, all should be same

#Draw the image again for create Title Text
