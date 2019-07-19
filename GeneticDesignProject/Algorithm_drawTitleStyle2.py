from PIL import ImageFont, ImageDraw, Image, ImageFilter
from Algorithm_Text import TextDrawShade

def drawTitleStyle2(imageSource = None,
                    bigText = "LinkGish",
                    littleText = "Innovation Center",
                    bigTextColor = (0,0,0,255),
                    littleTextColor = (255,255,255,255)
                        ):
    img = imageSource
    #Draw big text in title
    fontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Tulpen_One/TulpenOne-Regular.ttf'   #Open custom font
    fontSize = 1600     #Set font size
    font = ImageFont.truetype(fontPath,fontSize,0,"unic",None)  #Generate font
    titleText = bigText
    titleText = titleText.upper()     #Input title text
    textsize = font.getsize(titleText)   #Getting the width and height of the text
    # Making the big title
    canvas = Image.new('RGBA', (textsize[0]+300, textsize[1]), 0)
    draw = ImageDraw.Draw(canvas)
    draw.text((0,0), titleText, font = font, fill = bigTextColor)
    # canvas.show()

    #Draw a sub text below the big title
    # subFontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Marck_Script/MarckScript-Regular.ttf'   #Open custom font
    subFontPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Great_Vibes/GreatVibes-Regular.ttf'   #Open custom font
    subFontSize = 400
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
    CWidth = int(ratio*(canvas.size[0]-300))
    outputSize = int(ratio*fullCanvasSize[0]), int(ratio*fullCanvasSize[1])
    fullCanvas = fullCanvas.resize(outputSize ,Image.ANTIALIAS)
    # fullCanvas.show()
    print(fullCanvas.size)
    
    img.paste(fullCanvas, (int((img.size[0]-CWidth)/2), img.size[1]//4), fullCanvas)
    return img

