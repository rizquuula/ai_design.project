import numpy as np
from PIL import Image, ImageDraw

def testColorRange():
    first = (170, 84, 57),(40,119,79)
    second = (170,160,57),(75,45,115)
    third = (170,167,57),(84,43,114)

    listC = [first, second, third]
    for i in listC:
        for j in range(3):
            print(i[0][j]-i[1][j],' and ',i[0][j]+i[1][j], ' and ',i[0][j]*i[1][j],' and ',i[0][j]/i[1][j])
        print()
        print(np.sqrt( (i[0][0]-i[1][0])**2 + (i[0][1]-i[1][1])**2 + (i[0][2]-i[1][2])**2 ))
        print()

def test2ColorComb():
    blue = '#143D59'
    yellow = '#F4B41A'

    navy = '#213970'
    teal = '#210070'

    black = '#FFE042'
    orange = '#E71989'

    maroon = '#5B0E2D'
    peach = '#FFA781'

    purpleDeep = '#5E001F'
    blueLight = '#00E1D9'

    beige = '#F2BC94'
    brownDark = '#30110D'

    base = Image.new('RGBA', (500,500), color=purpleDeep)
    base2 = Image.new('RGBA', (300,300), color=blueLight)
    base.paste(base2,(0,0),base2)
    base.show()

test2ColorComb()