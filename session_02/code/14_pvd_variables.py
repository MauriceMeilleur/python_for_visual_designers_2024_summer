# 14_pvd_variables

# variables in code allow you to quickly read and understand your code and make changes easily

# let's draw a random-grey-colored chessboard with nested loops again to see why, first with hard math

newPage()
for row in range(8):
    tempY = row * 125 # = 1/8 * 1000, default PageBot canvas
    for col in range(8):
        tempX = col * 125
        fill(random())
        rect(tempX, tempY, 125, 125)
        
# but what if you want to change the number of squares x or y or both, or the size/porportions of the canvas?

canvasX = 1000
canvasY = 1000
numX = 8
numY = 8
sizeX = canvasX/numX
sizeY = canvasY/numY
# now you can make changes to the variable definitions and they will automatically update the rest of the code where they're used
# also note that you can define variables in terms of other variables depending on the relationships between them you want to operate in the code

newPage(canvasX, canvasY)
for row in range(numY):
    tempY = row * sizeY
    for col in range(numX):
        tempX = col * sizeX
        fill(random())
        rect(tempX, tempY, sizeX, sizeY)