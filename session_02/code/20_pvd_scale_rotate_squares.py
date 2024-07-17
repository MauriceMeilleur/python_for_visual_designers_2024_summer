# 20_pvd_scale_rotate_squares

numSquares = 50 # how many squares to draw
scaleValue = .9 # how much to scale the squares each loop
rotateValue = 4 # how much to rotate the squares each loop
squareSize = width() # the size of the first square

# shift the origin to the center of the canvas
translate(width()/2, height()/2)

# now loop through the numbers 0–mySquareCount
for myNumber in range(numSquares):
    # set a random fill color
    fill(random(), random(), random()) 
    # draw a rectangle at the center of the canvas
    rect(-squareSize/2, -squareSize/2, squareSize, squareSize)
    # scale the canvas by our scale value
    scale(scaleValue)
    # rotate the canvas by our rotation 
    rotate(rotateValue)