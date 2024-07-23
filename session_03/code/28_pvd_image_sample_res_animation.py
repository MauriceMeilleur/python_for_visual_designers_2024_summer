# 28_pvd_image_sample_res_animation

# we'll make a two-phase animation of the imagePixelColor() vector simplification

myImage = ImageObject('/Users/meilleur/Desktop/nasa_colorful_aurora.png')
# define the canvas size for the frames from the dimensions of the image
canvasX, canvasY = myImage.size()
numX, numY = 20, 15
# define the number of frames in our animation
frames = 10
# set a factor for changing the resolution in each frame
factor = .2

# phase 1 will start lower-res and enhance resolution, phase 2 will  start at the max res and decrease
# we'll make this with 4 (!) nested for-loops: the outermost loop for the phases (to run twice), then a loop for the frames in each phase (to run as many times as there are frames), then loops for the rows and columns to sample and draw rectangles for
for myPhase in range(2):
    # this code runs once per phase
    for myFrameNumber in range(frames):
        # this code runs once per frame, per phase
        # create a new page with the dimensions of the image
        newPage(canvasX, canvasY)
        # get the dimensions of each cell
        cellX, cellY = width()/numX, height()/numY
        # now we'll sample and draw
        for row in range(numY):
            # this code runs once per row per frame per phase
            for col in range(numX):
                # this code runs once per column per row per frame per phase
                # define the x and y coordinates of each rectangle
                myX = col * cellX
                myY = row * cellY
                # sample the color of the pixel in the image at these coordinates and set the fill to the sampled color
                fill(*imagePixelColor(myImage, (myX, myY)))
                # now draw a rectangle with that fill
                rect(myX, myY, cellX, cellY)
        # at this level we're out of the nested for-loops for sampling colors and drawing rectangles; before we draw another frame = loop through the frame count again we have to increase (first phase) or decrease (second phase) the resolution
        # int() is a Python function that removes the decimal fraction from a float and returns it as an integer (note: it doesn't round the number)
        # we're doing this because we have to loop through the ranges of numX and numY; they need to be integers for range() to work
        numX = int(numX + numX * factor)
        numY = int(numY + numY * factor) 
    
    # at this level we're at the end of the phase loop; now we have to invert factor so it works on the resolution in reverse for the second phase
    factor = -factor
    
saveImage('image_sample_resolution_animation.mp4')