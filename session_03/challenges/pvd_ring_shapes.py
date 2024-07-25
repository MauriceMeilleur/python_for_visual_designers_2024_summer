# a function to draw a simple triangle (note: this is not an equilateral triangle)
def drawTriangleFromCenter(size):
    # a triangle is a three point polygon
    polygon((-size/2, 0), (size/2, 0), (0, size))

# a function to draw a ring of shapes, in this case a triangle
def drawRing(numShapes=10, size=100, offset=10):
    with savedState():
        for shape in range(numShapes):
            with savedState():
                translate(0, offset)
                drawTriangleFromCenter(size)
            rotate(360/numShapes)

shapeOffset = 10
shapeCount = 6
shapeSize = 5
ringCount = 50

newPage()
fill(1)
rect(0, 0, width(), height())

translate(width()/2, height()/2)

# add a shadow to all shapes
shadow((-2, 2), 5, (0, 0, 0, .1))

# loop through the number of rings we want to draw
for ring in range(ringCount):
    # make each ring a different color
    fill(random(), random(), random())
    # draw our ring of shapes
    drawRing(shapeCount, shapeSize, shapeOffset)
    # now augment our variables so the next ring will be drawn with more shapes
    shapeCount += 3
    # that are slightly larger
    shapeSize += 2
    # and increase the offset so each ring is drawn larger
    shapeOffset += shapeSize
    
saveImage('ring_of_shapes.png')