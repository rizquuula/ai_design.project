from PIL import Image, ImageDraw, ImageFilter


def make_ellipse_mask(size, x0, y0, x1, y1, blur_radius):
    img = Image.new("L", size, color=0)
    print(size)
    draw = ImageDraw.Draw(img)
    draw.ellipse((x0, y0, x1, y1), fill=255)
    return img.filter(ImageFilter.GaussianBlur(radius=blur_radius))


kitten_image = Image.open("/home/linkgish/Desktop/WebApp2/GeneticDesignProject/example2.jpg")
overlay_image = Image.new("RGB", kitten_image.size, color="orange")  # This could be a bitmap fill too, but let's just make it orange
mask_image = make_ellipse_mask(kitten_image.size, 150, 70, 350, 250, 5)
masked_image = Image.composite(overlay_image, kitten_image, mask_image)
print(overlay_image.size, kitten_image.size, mask_image.size)
masked_image.show()