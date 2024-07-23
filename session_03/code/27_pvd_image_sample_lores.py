# 27_pvd_image_sample_lores

imageName = '/Users/meilleur/Desktop/nasa_colorful_aurora.png'
myImage = ImageObject(imageName)
print(myImage.size())
newPage(*myImage.size())

# define the dimensions of a grid
numX, numY = 120, 90
# calculate cell dimensions for the grid based on canvas size and row/col count
cellX, cellY = width()/numX, height()/numY

# now we'll set up nested for-loops; we have to use absolute coordinates here, we can't translate our way arond the image
for row in range(numY):
    # loops through each row
    for col in range(numX):
        # loops through each column in each row
        # we'll define x and y values to position the rectangles we're going to draw by multiplying the column/row count by the cell sizes
        myX = col * cellX
        myY = row * cellY
        # now we'll sample the color of the pixel in the image at (x, y) and set the fill color to that color, unpacking the 4-tuple RGBalpha and feeding the values to fill()
        fill(*imagePixelColor(myImage, (myX, myY)))
        # and we'll draw a rectangle
        rect(myX, myY, cellX, cellY)