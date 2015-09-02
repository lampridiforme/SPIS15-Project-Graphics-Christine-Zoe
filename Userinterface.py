from PIL import Image, ImageDraw, ImageTk
import random
##zebra = Image.open("zebra.jpg")
##photo = Image.open("photo.png")
##sample = Image.open("green-screen.jpg")
##photo1 = Image.open("thatme.jpg")
photo2 = Image.open("photo2.jpg")
WithGreen= Image.open("meWithGreen.png")
##ohno = Image.open("ohno.jpg")
##beach = Image.open("beach.jpg")
##test = Image.open("test.png")
##croptest = Image.open("testForCropping.png")

def getComposite(im, thresh, x, y):
    """Gets the sum of all RGB values and returns as a composite."""
    (red,green,blue) = im.getpixel((x,y)) 
    redResult = abs(red - thresh[0])
    greenResult = abs(green - thresh[1])
    blueResult = abs(blue - thresh[2])
    composite = (redResult + greenResult + blueResult)
    return (redResult + greenResult + blueResult)

def removeBackground(im):
    """Removes green and applies white"""
    (width,height) = im.size
    for x in range(0,width):
        for y in range(0,height):
            thresh = [157, 190, 75]
            comp = getComposite(im, thresh, x, y)
            if  comp < 85:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [100, 140, 75]
            comp = getComposite(im, thresh, x, y)
            if  comp < 55:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [60, 100, 25]
            comp = getComposite(im, thresh, x, y)
            if  comp < 55:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [0,230,0]
            comp = getComposite(im, thresh, x, y)
            if  comp < 100:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [0,255,50]
            comp = getComposite(im, thresh, x, y)
            if  comp < 100:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [96, 140, 75]
            comp = getComposite(im, thresh, x, y)
            if  comp < 40:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [89, 97, 45]
            comp = getComposite(im, thresh, x, y)
            if  comp < 35:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [100, 132, 255]
            comp = getComposite(im, thresh, x, y)
            if  comp < 50:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [213, 210, 103]
            comp = getComposite(im, thresh, x, y)
            if  comp < 50:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [142, 139, 44]
            comp = getComposite(im, thresh, x, y)
            if  comp < 60:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
            thresh = [242, 231, 113]
            comp = getComposite(im, thresh, x, y)
            if  comp < 50:
                newRed = 0
                newGreen = 255
                newBlue = 0
                im.putpixel((x, y), (newRed, newGreen, newBlue))
    im.show()
    im.save("meWithGreen.png")


##Create function that takes the background and replaces the bright green
##PROBLEM: Function takes at least 30 seconds to run, speed up somehow.
def getBackData(back, fore):
    """Replaces green with background image."""
##Initialize images
    draw = ImageDraw.Draw(back)
    draw = ImageDraw.Draw(fore)
##Turns background neon green to increase contrast
    removeBackground(fore)
    (width, height) = fore.size
##Conditional statement deciding whether or not the background is large enough. 
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




def transparency(image):
    image = image.convert("RGBA")
    pixdata = image.load()
    for y in xrange(image.size[1]):
        for x in xrange(image.size[0]):
            if pixdata[x, y] == (0, 255, 0, 255):
                pixdata[x, y] = (255, 255, 255, 0)
    image.show()
    image.save("trans1.png", "PNG")


import Tkinter
from Tkinter import Tk, Label, CENTER, Canvas, NW

app=Tk()
beach = Image.open("beach.jpg")
Zoe = Image.open("trans1.png")


canvas=Canvas(app,width=beach.size[0],height=beach.size[1])
canvas.pack()



app.title ("Chroma key tool")
photo=ImageTk.PhotoImage(beach)
canvas.create_image((0,0), image= photo, anchor=NW)
photo1=ImageTk.PhotoImage(Zoe)
zoeid= canvas.create_image((0,0), image= photo1, anchor=NW)
#canvas.move(zoeid, )


def key(event):

    global scaling_factor
    if event.char == '>':
        scaling_factor = scaling_factor + 0.1
        resize()
    

    elif event.char == '<':
        scaling_factor = scaling_factor - 0.1
        resize()

    elif event.char=="<Right>":
        x=x+5
        print x
    

    #elif event.char
    
(x,y)=canvas.coords(zoeid)
##if
canvas.bind("<Right>", lambda event:canvas.move(zoeid,5,0))
##    x=x+5


canvas.bind("<Left>", lambda event:canvas.move(zoeid,-5,0))

canvas.bind("<Up>", lambda event:canvas.move(zoeid,0,-5))

canvas.bind("<Down>", lambda event:canvas.move(zoeid,0,5))
canvas.focus_set()

canvas.bind("<Key>", key)
    #print canvas.coords(zoeid)
    #coords

scaling_factor = 1.0

def resize():
    global canvas, zoeid, photo1, Zoe, scaling_factor, coorx, coory,x,y
    (x,y)= canvas.coords(zoeid)
    
    if zoeid:
        canvas.delete(zoeid)

    size = int(scaling_factor * Zoe.size[0]), int(scaling_factor * Zoe.size[1])
    photo1 = ImageTk.PhotoImage(Zoe.resize(size))
    zoeid= canvas.create_image((x,y), image=photo1)

app.mainloop()




