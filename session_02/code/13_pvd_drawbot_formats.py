# 13_pvd_drawbot_formats

# DrawBot has a number of built-in format definitions for canvasses

print(width(), height())

# help(newPage)
print(sizes())

newPage('Letter')
print(width(), height())

numX = 8
numY = 8
sizeX = width()/numX
sizeY = height()/numY

for row in range(numY):
    tempY = row * sizeY
    for col in range(numX):
        tempX = col * sizeX
        fill(random())
        rect(tempX, tempY, sizeX, sizeY)
        
# notes:
# newDrawing() will clean out the entire stack of canvasses, sometimes useful between saveImage() calls
# size() creates a single canvas only, you have to call newDrawing() before using again—it isn't very useful for what we're doing