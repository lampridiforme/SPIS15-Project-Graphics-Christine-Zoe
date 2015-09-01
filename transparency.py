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


def transparency(image):
    image = image.convert("RGBA")
    pixdata = image.load()
    for y in xrange(image.size[1]):
        for x in xrange(image.size[0]):
            if pixdata[x, y] == (0, 255, 0, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    image.show()
    image.save("img2.png", "PNG")

#YESSSS IT WORKS
#Code credit: http://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent 
