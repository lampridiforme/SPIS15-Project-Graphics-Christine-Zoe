from PIL import Image, ImageDraw
import random
zebra = Image.open("zebra.jpg")
photo = Image.open("photo.png")
sample = Image.open("green-screen.jpg")
photo1 = Image.open("thatme.jpg")
photo2 = Image.open("photo2.jpg")
ohno = Image.open("ohno.jpg")
beach = Image.open("beach.jpg")
test = Image.open("test.png")
croptest = Image.open("testForCropping.png")

def crop(image, startx, starty, endx, endy):
    image.crop((startx, starty, endx, endy))
    image.show()
    image.save("img2.png", "PNG")

def cropMark2(image):
    outfile = "croppedImage.jpg"
    image.copy()

    crop_img = image.crop((0, 0, 500, 500))
    crop_img.thumbnail((100,100), Image.ANTIALIAS)
    crop_img.save(outfile, "JPEG")
    
