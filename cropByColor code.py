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

#PROBLEM: FIGURE OUT WHY THERE IS A NONETYPE ERROR WHEN USING ANY IMAGE OTHER THAN "test.png"
def findLeftPixels(image):
    x = 0
    y = 0
    (width, height) = image.size
    for x in range(0,width):
        (red,green,blue) = image.getpixel((x,y))
        if (red, green, blue) != (0,255,0):
            return x

def findTopPixels(image):
    x = 0
    y = 0
    (width, height) = image.size
    for x in range(0,height):
        (red,green,blue) = image.getpixel((x,y))
        if (red, green, blue) != (0,255,0):
            return y

def findRightPixels(image):
    x = 0
    y = 0
    (width, height) = image.size
    leftPixel = findLeftPixels(image)
    for x in range(leftPixel, width):
        (red,green,blue) = image.getpixel((x,y))
        if (red, green, blue) == (0,255,0):
            return x
                
def findBottomPixels(image):
    x = 0
    y = 0
    topPixel = findTopPixels(image)
    (width, height) = image.size
    for y in range(topPixel, height):
        (red,green,blue) = image.getpixel((x,y))
        if (red,green,blue) == (0,255,0):
            return y

##PROBLEM: CROP DOES NOT SEEM TO WORK IN ANY INSTANCE- NEED TO WRITE OWN CROP FUNCTION?
def minimalCrop(image):
    (width, height) = image.size
    left = findLeftPixels(image)
    right = findRightPixels(image)
    top = findTopPixels(image)
    bottom = findBottomPixels(image)
##    left = int(left)
##    right = int(right)
##    top = int(top)
##    bottom = int(bottom)
##    image.crop((0,0,width, top))
##    image.crop((0,bottom, width, height))
##    image.crop((0,top, left, bottom))
##    image.crop((right, top, width, bottom))
    cropped = image.crop((left, top, right, bottom))
    image.show(cropped)

##def crop(image, top, bottom, left, right):
##    draw = ImageDraw.Draw(image)
##    #Set image width and height
##    (width,height) = image.size
##    for x in range(0,width):
##        for y in range(0,height):
##            
    
