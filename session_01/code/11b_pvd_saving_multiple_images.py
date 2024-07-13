# let's try another 'animation', now a field of letters in random colors and positions we'll draw on a series of canvasses and save as an animated .gif and an .mp4

myString = 'the quick brown fox'
numPages = 60

for page in range(numPages):
    newPage()
    # frameDuration() is a DrawBot function that records for the current canvas how long it will last as a frame in a motion graphic file
    # it takes a single argument, a fraction of a second; 1 = 1 frame per second, 1/12 = 12 frames per second, etc
    frameDuration(1/12)
    # set the font size for the letters we're going to draw
    fontSize(130)
    for myLetter in myString:
        # define two variables for random horizontal and vertical positions on the canvas
        tempX = randint(0, width())
        tempY = randint(0, height())        
        # define a random r, g, b fill color like we did in the last sketch
        fill(random(), random(), random())        
        # draw our text on the canvas at the random x, y coordinates
        text(myLetter, (tempX, tempY))

saveImage('~/Desktop/random_letters_animation.gif')
saveImage('~/Desktop/random_letters_animation.mp4')