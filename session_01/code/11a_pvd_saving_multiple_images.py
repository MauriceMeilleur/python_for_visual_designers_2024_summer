# let's try an 'animation', really just a field of circles in random colors we'll draw on a series of canvasses and save as an animated .gif and an .mp4

# first we'll define some variables (I did the math for you!)
numSquares = 8 # the field will be 8x8
sqSize = 94
space = 21
margin = 60

# and here's a variable for the number of pages to make, which will be the number of frames in the animation
numPages = 60

# now we'll nest two loops inside a third: the most outside loop will be the loop that draws each canvas (60); inside the canvas/frame loop will be the loop that draws each row of shapes (starting from the bottom); and inside the row loop will be the loop that draws the shapes in each column position
# again, pay attention to the indents! they'll tell you where you are in the loops in the code

for page in range(numPages):
    # code at this level will run 60 times, one for each frame
    newPage() # we'll use the DrawBot defaults to set up each frame
    for row in range(numSquares):
        # code at this level will run 8 times per frame, once for each row
        y = row * (sqSize + space) + margin
        for col in range(numSquares):
            # code at this level will run 8 times per row, once for each column
            x = col * (sqSize + space) + margin
            fill(random(), random(), random()) 
            oval(x, y, sqSize, sqSize)
            
# Drawbot automatically knits all the canvasses together for file formats that take multiple frames
saveImage('~/Desktop/random_circles_animation.gif')
saveImage('~/Desktop/random_circles_animation.mp4')