import cv2
import numpy as np 
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from Algorithm_BackgroundManipulation import makeGradientImage, GammaCorrection, pasteTransparentImage
from Algorithm_PIL_cv2 import PILtoCV2, CV2toPIL
from Algorithm_bannerText import drawBannerTitle
from Algorithm_colorMaterial import LIGHTorDARK
from Algorithm_logoMaker import imgResizer
from Algorithm_backgroundSelection import backgroundSelection
from time import ctime

bannerX = 3
bannerY = 1

scale = 1000

bannerX, bannerY = bannerX*scale, bannerY*scale

# Making canvas for banner 
banner = Image.new('RGBA', (bannerX,bannerY), color=(222,222,222,255))
# Make gradient color for overlay color
gradOverlay = makeGradientImage(width=bannerX,
                            height=bannerY,
                            # initialR=100,
                            # initialG=100,
                            # initialB=20,
                            ) # This is PIL
gradOverlay = PILtoCV2(image=gradOverlay)
gradOverlay = GammaCorrection(image=gradOverlay,
                            gamma=0.3,
                            ) # This is cv2
gradOverlay = CV2toPIL(image=gradOverlay).convert('RGBA')
# gradOverlay.show()
# banner.paste(gradOverlay,(0,0),gradOverlay)
# Paste transparent image as mask
banner = pasteTransparentImage(image=banner,
                        overlayImage= backgroundSelection(category='City'),
                        percentTransparency=50)

# Paste Overlay image as transparency mask
banner = pasteTransparentImage(image=banner,
                        overlayImage=gradOverlay,
                        percentTransparency=50)
# Make banner main title
banner = drawBannerTitle(image=banner,
                    fontPath='/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Font-lib/Archivo_Black/ArchivoBlack-Regular.ttf',
                    text='workshop kepenulisan',
                    ratioWidth=40,
                    ratioHeight=600,
                    pasteXratio=10,
                    pasteYratio=50,
                    percentTransparency=80,
                    fontColor= (222,222,222), # LIGHTorDARK(image=imageCv2),
                    )
# import trapesium for dim some area
trapesium = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Object-lib/trapesium-black-crop.png')
trapesium = imgResizer(img=trapesium,
                    targetHeight=banner.size[1])    # resizing the height

# paste the trapesium overlay the banner image
banner = pasteTransparentImage(image=banner,
                        overlayImage=trapesium,
                        percentTransparency=25,
                        pasteX=int((30/100)*banner.size[0]),
                        )
# Use time as a unique file name, so it will not be duplicated in the future
nowTime = ctime()
# Input variable of time into the string 
savePath = ('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Result-lib/BannerStyle1/Style1 {}.jpg').format(nowTime)
banner = banner.convert('RGB')
banner.save(savePath)
print('Successfully saved at : ',savePath) # Notification while done

# Creating thumbnail from a large size banner 
targetThumbnailX = 900
Tratio = targetThumbnailX/bannerX
thumbnailSize = int(bannerX*Tratio),int(bannerY*Tratio)
banner.thumbnail((thumbnailSize))
banner.show()
# gradOverlay.thumbnail((thumbnailSize))
# gradOverlay.show()
