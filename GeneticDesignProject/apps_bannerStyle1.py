import cv2
import numpy as np 
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from Algorithm_BackgroundManipulation import imgResizer, makeGradientImage, GammaCorrection, pasteTransparentImage
from Algorithm_PIL_cv2 import PILtoCV2, CV2toPIL
from Algorithm_bannerText import drawBannerTitle, drawBannerDetail
from Algorithm_colorMaterial import LIGHTorDARK
from Algorithm_logoMaker import  drawOranizerLogo, drawSponsorshipLogo
from Algorithm_backgroundSelection import backgroundSelection
from Algorithm_Sosmed import drawAnotherSosmed
from time import ctime

bannerX = 4
bannerY = 2

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
                    percentTransparency=90,
                    fontColor= (222,222,222), # LIGHTorDARK(image=imageCv2),
                    )
# import trapesium for dim some area
trapesium = Image.open('/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Object-lib/trapesium-black-crop.png')
trapesium = imgResizer(img=trapesium,
                    targetHeight=banner.size[1])    # resizing the height

# paste the trapesium overlay the banner image
banner = pasteTransparentImage(image=banner,
                        overlayImage=trapesium,
                        percentTransparency=15,
                        pasteX=int((30/100)*banner.size[0]),
                        )
# print(banner)
banner = drawBannerDetail(image=banner,
                        placeText = 'Ruang H5, Gedung H, Fakultas Teknik, UNILA, Kota Bandar Lampung, Lampung, Indonesia',
                        dateText = 'Senin, 13 Agustus 2019',
                        timeText = 'Pukul 08.00 s.d. 16.00 WIB',
                        ratioXpaste=65,
                        ratioXsize=30,
                        )

banner = drawAnotherSosmed(#isTrue=False,
                        image=banner,
                        ratioHeight = 3,
                        useOverlay = True,
                        forceColor= (255,255,255,255),
                        account_IG = '@FSLDKLampung' ,
                        account_FB = 'Puskomda FSLDK Lampung' ,
                        account_WA = None ,
                        account_LINE = None ,
                        account_TELEGRAM = None ,
                        account_WEB = 'https://fsldklampung.id' ,
                        account_TWITTER = 'FSLDK Lampung',
                        account_YOUTUBE = None,
                        ratioXpaste = 80,
                        ratioYpaste = 92,
                    )

biiLogoPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Logo-birohmah.png'
fsldkLogoPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-fsldklampung.png'
unilaLogoPath = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/logo-unila.png'
banner = drawOranizerLogo(image=banner,
                        logo_1=unilaLogoPath,
                        logo_2=biiLogoPath,
                        logo_3=fsldkLogoPath,
                        pasteXRatio=5,
                        pasteYRatio=5,
                        sizeYratio=7,
                        backTransparency = 85,
                        backColor='white',
                        )
                        
banner = drawSponsorshipLogo(image = banner,
                        ratioXpaste=4,
                        ratioYpaste=95,
                        logoRow=3,
                        logo1 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/a.png',
                        logo2 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/b.png',
                        logo3 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/c.png',
                        logo4 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/d.png',
                        logo5 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/e.jpg',
                        logo6 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/f.png',
                        logo7 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/g.png',
                        logo8 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/h.png',
                        logo9 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/ff.png',
                        logo10 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/gg.png',
                        logo11 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/hh.png',
                        logo12 = '/home/linkgish/Desktop/WebApp2/GeneticDesignProject/Image-lib/Logo-lib/Sponsorship/ff.png',
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
