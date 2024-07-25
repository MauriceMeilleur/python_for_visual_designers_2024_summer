# make a function to draw a circle that only requires a width and height
def centerOval(wide, high):
    oval(-wide/2, -high/2, wide, high)

# set some variables
numX = 10 # number of cols
numY = 10 # number of rows
cellX = width()/numX # width of each col
cellY = height()/numY # width of each row
shapeSize = cellX * .75 # drw the shape at 3/4 the grid size, give 
sizeVar = int(shapeSize/10) # vary each shape randomly by by about 10%

newPage()
fill(1, 0, 1)
rect(0, 0, width(), height())
fill(0)

# a slightly different way to translate() through a grid
translate(cellX/2, cellY/2)
# loop through rows
for row in range(numY):
    with savedState():
        for col in range(numX):
            # get a number between -sizeVar and sizeVar
            var = randint(-sizeVar, sizeVar)
            # get the size from the basic size and random variation
            size = shapeSize + var
            # draw the oval
            centerOval(size, size)
            # move to the right
            translate(cellX, 0)
    translate(0, cellY)

saveImage('pattern_example_polkadot.png')