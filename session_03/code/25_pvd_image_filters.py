imageName = '/Users/meilleur/Desktop/crystal_lake.jpg'
myImage = ImageObject(imageName)

# there are a number of image filters built into DrawBot: drawbot.com/content/image/imageObject.html

# myImage.sepiaTone(0)
# myImage.vignette(100, 10)
# myImage.kaleidoscope(9)
myImage.photoEffectNoir()

# set the canvas to the image size, unpacking the width and height
newPage(*myImage.size())
# draw the modified image to canvas
image(myImage, (0, 0))

# once you apply a filter to an imageObject, you change the object
myImage.sepiaTone(0)
newPage(*myImage.size())
# draw the modified image to canvas
image(myImage, (0, 0))

# so you can make a copy of the object first
imageName = '/Users/meilleur/Desktop/crystal_lake.jpg'
myImage = ImageObject(imageName)
# to make a new object as a copy of an existing one, you have to use the method object.copy(); myBackup = myImage just assigns a second name to the same object in memory
myBackup = myImage.copy()

newPage(*myImage.size())
image(myImage, (0, 0))

newPage(*myBackup.size())
myBackup.sepiaTone(0)
image(myBackup, (0, 0))
