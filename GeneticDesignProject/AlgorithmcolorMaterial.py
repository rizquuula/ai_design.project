import random

red = (239, 83, 80)
pink = (236, 64, 122)
purple = (171, 71, 188)
deep_purple = (126, 87, 194)
indigo = (92, 107, 192)
blue = (66, 165, 245)
light_blue = (41, 182, 246)
cyan = (38, 198, 218)
teal = (38, 166, 154)
green = (102, 187, 106)
light_green = (156, 204, 101)
lime = (212, 225, 87)
yellow = (255, 238, 88)
amber = (255, 202, 40)
orange = (255, 167, 38)
deep_orange = (255, 112, 67)
brown = (141, 110, 99)
grey = (255,255,255)#(189, 189, 189)
blue_grey = (120, 144, 156)

# Function to ram=ndomize the color from database
def random2MaterialColor():
    listColor = [red, pink, purple, deep_purple, indigo, blue, light_blue, cyan,
                    teal, green, light_green, lime, yellow, amber, orange, deep_orange,
                    brown, grey, blue_grey]
    count = len(listColor)
    # print(count)
    num = random.randint(0,count-1)
    num2 = random.randint(0,count-1)
    result = listColor[num]
    result2 = listColor[num2]
    print(result, ' and ', result2)
    return result, result2

# Function to select color form database by it name
def selectColor(color=None):
    listColorStr = ['red', 'pink', 'purple', 'deep_purple', 'indigo', 'blue', 'light_blue', 'cyan',
                    'teal', 'green', 'light_green', 'lime', 'yellow', 'amber', 'orange', 'deep_orange',
                    'brown', 'grey', 'blue_grey']
    listColor = [red, pink, purple, deep_purple, indigo, blue, light_blue, cyan,
                    teal, green, light_green, lime, yellow, amber, orange, deep_orange,
                    brown, grey, blue_grey]
    if color in listColorStr:
        selected = listColorStr.index(color)
        result =  listColor[selected]
    else:
        result = (255,255,255)

    return result

    

# randomMaterialColor()