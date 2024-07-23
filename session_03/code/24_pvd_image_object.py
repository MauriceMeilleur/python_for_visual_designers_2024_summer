# 24_pvd_image_object

# we'll create a variable with a value which is a string, the path to the image we want to open
# remember we can drag not just folders, but also files into the coding window in DrawBot to capture their paths
imageName = '/Users/meilleur/Desktop/crystal_lake.jpg'

# image() is a Drawbot function that draws a specified image on the canvas; it takes two arguments, a string for the path to the image and a 2-tuple for the x, y position of the image 
# but if we just draw the image on the default canvas, it may not fit
image(imageName, (0, 0))

# so we'll define an imageObject() using the variable, but we won’t draw it to canvas yet
myImage = ImageObject(imageName)

# the image now exists as an object in memory, even if we don’t see it on the canvas; we can get information about that object, like its dimensions
print(myImage.size())

# and we can use that informtion to set the canvas size; remember the Python operator * 'unpacks' the tuple with the image width and height, we pass those as arguments to newPage() as separate values
newPage(*myImage.size())

# with the canvas the correct size we can draw the image on it so it will fit properly
image(myImage, (0, 0))