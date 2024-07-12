# you can run a for-loop inside another for-loop; remember to pay attention to your indents, since Python uses the level of indent to keep track of what code runs when
# the nice thing is that the indents make it easier for you to read (and troubleshoot) your code

# pay attention to the indent levels of the comments!

# let's make a weird chessboard
# we'll divide the default canvas into 64 squares, 8x8
newPage()
# we'll define the dimensions of the squares as fractions of the dimensions of the canvas
sWidth = width()/8
sHeight = height()/8
# and the squares are offset from each other by their own dimensions; they're the same wide and high, so we'll just pick one dimension to use
offset = sWidth
# now let's set up the loops
for y in range(8): # let's call this the outside loop
    # we'll use y for the name of the temporary variable for this loop, because this loop is going to move us through the vertical dimension of the canvas
    yTemp = y * offset # the temporary y position will start at 0 * offset = 0 and go up by the value of the offset each time this loop runs
    # now we're going to nest a second for-loop inside the first:
    for x in range(8): # let's call this the inside loop
        xTemp = x * offset # the temporary x position will start at 0 * offset = 0 and go up by the value of the offset each time this loop runs
        # set a random fill color
        fill(random(), random(), random())
        # and draw a square—at the position xTemp, yTemp and with the dimensions sWidth, sHeight
        rect(xTemp, yTemp, sWidth, sHeight) 
        # now, all the code inside the inside loop will run, and then the computer will look to see if there's anything left in the sequence for the inside loop—if yes, it will run the code in the inside loop again, with the next value of x; and it will keep running the inside loop code, changing the value of xTemp each time
        # when it doesn't see anything left in the sequence for the inside loop …
    # then and only then it will exit the inside loop and look to see if there's any code left to run for the *outside* loop; if not, or when it's run that additional code (there isn't any in this sketch), then it will look to see if there's anything left in the sequence for the outside loop
    # if there is, then it will run the code for the outside loop again, now with a new value for yTemp
    # and when it gets to the function call for the inside loop …
        # it will run the code in the inside loop over and over again, again, until the sequence for the inside loop is exhausted …
    # and then pop out to the outside loop again
    # once the sequence for the outside loop is exhausted …
# then and only then it will exit the outside loop and look for any code below it
print('The crazy-colored chessboard is drawn!')