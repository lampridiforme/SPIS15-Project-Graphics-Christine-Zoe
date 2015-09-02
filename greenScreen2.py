from PIL import Image, ImageDraw
import random
zebra = Image.open("zebra.jpg")
photo = Image.open("photo.png")
sample = Image.open("green-screen.jpg")
photo1 = Image.open("thatme.jpg")
photo2 = Image.open("photo2.jpg")
ohno = Image.open("ohno.jpg")
beach = Image.open("beach.jpg")

def getComposite(im, thresh, x, y):
    """Gets the sum of all RGB values and returns as a composite."""
    (red,green,blue) = im.getpixel((x,y)) 
    redResult = abs(red - thresh[0])
    greenResult = abs(green - thresh[1])
    blueResult = abs(blue - thresh[2])
    return (redResult + greenResult + blueResult)

def aLotOfTests(im, x, y):
    thresh = [157, 190, 75]
    comp = getComposite(im, thresh, x, y)
    if  comp < 85:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [100, 140, 75]
    comp = getComposite(im, thresh, x, y)
    if  comp < 55:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [60, 100, 25]
    comp = getComposite(im, thresh, x, y)
    if  comp < 55:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [0,230,0]
    comp = getComposite(im, thresh, x, y)
    if  comp < 100:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [0,255,50]
    comp = getComposite(im, thresh, x, y)
    if  comp < 100:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [96, 140, 75]
    comp = getComposite(im, thresh, x, y)
    if  comp < 40:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [89, 97, 45]
    comp = getComposite(im, thresh, x, y)
    if  comp < 35:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [100, 132, 255]
    comp = getComposite(im, thresh, x, y)
    if  comp < 50:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [213, 210, 103]
    comp = getComposite(im, thresh, x, y)
    if  comp < 50:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [142, 139, 44]
    comp = getComposite(im, thresh, x, y)
    if  comp < 60:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return
    thresh = [242, 231, 113]
    comp = getComposite(im, thresh, x, y)
    if  comp < 50:
        newRed = 0
        newGreen = 255
        newBlue = 0
        im.putpixel((x, y), (newRed, newGreen, newBlue))
        return

def removeBackground(im):
    """Removes green and applies white"""
    (width,height) = im.size
    for x in range(0,width):
        for y in range(0,height):
            aLotOfTests(im, x, y)
    im.show()


def resizeImage(back, fore):
    (x,y) = fore.size
    (width, height) = back.size
    back = back.resize((x + 10, y +10),Image.ANTIALIAS)
    
            
##Create function that takes the background and replaces the bright green
##PROBLEM: Function takes at least 30 seconds to run, speed up somehow.
def resizeGreenscreen(back, fore):
    """Replaces green with background image."""
##Initialize images
    draw = ImageDraw.Draw(back)
    draw = ImageDraw.Draw(fore)
##Turns background neon green to increase contrast
    removeBackground(fore)
    (width, height) = fore.size
    back = back.resize((width + 10, height +10),Image.ANTIALIAS)
##Loop containing the width and height of the foreground
    for x in range(width):
        for y in range(height):
##Set the RGB values for the back pixels to a variable
            (r,g,b) = back.getpixel( (x, y) )
            br = r
            bg = g
            bb = b
##Set the RGB values for the front pixels to a variable
            (r,g,b) = fore.getpixel( (x, y) )
            fr = r
            fg = g
            fb = b
##If the value is bright green, replace with the background pixels stored in the variable
            if (fr, fg, fb) == (0, 255, 0):
                fore.putpixel((x, y),(br,bg,bb))
    fore.show()
    fore.save("greenscreenfinished.png")

def printSize(im):
    """Prints the size of the image."""
    draw = ImageDraw.Draw(im)
    (x,y) = im.size
    print x
    print y
    return
##    print getComposite(im, thresh, x, y)



                
##    thresh = [60, 100, 25]
##    for x in range(0,width):
##        for y in range(0,height):
##            (red,green,blue) = im.getpixel((x,y))
##            redResult = abs(red - thresh[0])
##            greenResult = abs(green - thresh[1])
##            blueResult = abs(blue - thresh[2])
##            composite = (redResult + greenResult + blueResult)
##            if  composite < 60:
##                newRed = 255
##                newGreen = 255
##                newBlue = 255
##                im.putpixel((x, y), (newRed, newGreen, newBlue))
 
    
    #Draw image        
    

def pixelColor(x,y):
    return photo.getpixel((x,y))

