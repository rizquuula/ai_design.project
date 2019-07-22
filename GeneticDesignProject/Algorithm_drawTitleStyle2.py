from PIL import ImageFont, ImageDraw, Image, ImageFilter
from Algorithm_Text import TextDrawShade

# Draw the main text that constructed by Bid and Little text
def drawTitleStyle2(imageSource = None,
                    bigText = "LinkGish",
                    littleText = "Innovation Center",
                    bigTextColor = (0,0,0,255),
                    littleTextColor = (255,255,255,255),
                    bigFontSize = 1300,
                    littleTextSize = 600,
                        ):
    # Aliasing to 'img'
    img = imageSource
    #Draw big text in title
    fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Tulpen_One/TulpenOne-Regular.ttf'   #Open custom font
    fontSize = bigFontSize     #Set font size
    font = ImageFont.truetype(fontPath,fontSize,0,"unic",None)  #Generate font
    titleText = bigText
    titleText = titleText.upper()     #Input title text
    textsize = font.getsize(titleText)   #Getting the width and height of the text
    # Making the big title and add some padding for the little text
    canvas = Image.new('RGBA', (textsize[0]+300, textsize[1]), 0)
    draw = ImageDraw.Draw(canvas)
    draw.text((0,0), titleText, font = font, fill = bigTextColor)
    # canvas.show()

    #Draw a sub text below the big title
    # subFontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Marck_Script/MarckScript-Regular.ttf'   #Open custom font
    subFontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Great_Vibes/GreatVibes-Regular.ttf'   #Open custom font
    subFontSize = littleTextSize
    subFont = ImageFont.truetype(subFontPath, subFontSize)
    subText = littleText
    subTextSize = subFont.getsize(subText)
    
    #MAking sub title 
    subCanvas = Image.new('RGBA', (subTextSize[0]+100, subTextSize[1]), 0)
    drawSubs = ImageDraw.Draw(subCanvas)
    drawSubs.text((100,0), subText, font=subFont, fill=littleTextColor)
    subCanvas = subCanvas.rotate(5, expand=5)
    print(subCanvas.size[0], ' and ', canvas.size[0])

    # to press the size of subs fit to big title
    if subCanvas.size[0] > canvas.size[0]:
        R = canvas.size[0]/subCanvas.size[0]
        NS = int(R*subCanvas.size[0]), int(R*subCanvas.size[1])
        subCanvas = subCanvas.resize(NS, Image.ANTIALIAS)

    # subCanvas.show()

    #Making the full paste title and sub
    fullCanvasSize = (canvas.size[0], canvas.size[1]+int(0.5*subCanvas.size[1]))
    fullCanvas = Image.new('RGBA', (fullCanvasSize), 0)
    fullCanvas.paste(canvas, (0,0), canvas)
    fullCanvas.paste(subCanvas, (fullCanvasSize[0]-subCanvas.size[0], fullCanvasSize[1]- int(subCanvas.size[1])), subCanvas)

    # Change the size 
    ratio = (img.size[1]/4)/fullCanvasSize[1]
    print('Ratio = ',ratio)
    CWidth = int(ratio*(canvas.size[0]-300))
    outputSize = int(ratio*fullCanvasSize[0]), int(ratio*fullCanvasSize[1])
    fullCanvas = fullCanvas.resize(outputSize ,Image.ANTIALIAS)
    print('Full title text size = ', fullCanvas.size)
    # fullCanvas.show()

    # If the size is too large, it will forced to fit the maximum size 
    if (fullCanvas.size[0]>(img.size[0]*2/3)):
        W_ratio = (img.size[0]*0.6) / fullCanvas.size[0]
        CWidth = CWidth*W_ratio
        print('W ratio', W_ratio)
        newSize = int(W_ratio*fullCanvas.size[0]), int(W_ratio*fullCanvas.size[1])
        fullCanvas = fullCanvas.resize(newSize ,Image.ANTIALIAS)

    print('Full title text size = ', fullCanvas.size)
    # Paste to the background image
    img.paste(fullCanvas, (int((img.size[0]-CWidth)/2), img.size[1]//4), fullCanvas) 
    
    return img

