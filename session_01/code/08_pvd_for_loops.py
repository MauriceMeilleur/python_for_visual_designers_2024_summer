# let's loop through a sequence, doing something with each item in a sequence one at a time
# this is called a 'for-loop' and it's an important tool in coding

# create a variable called myString
myString = 'Hello world!'

# loop through each character in the string
# myLetter is a variable we create that will be equal to the current item in the sequence
# this is a temporary variable—we can call it anything as long as it's not a protected (already-used) name in DrawBot or Python, good practice is to call it something meaningful in the context of what you're doing with the code
for myLetter in myString:   
    # all code that is indented immediately below the for-loop function call will run once for each item in the sequence being looped through
    # the code will print each character (element) in the string, one at a time
    # remember that in a string, a space is also a character
    print(myLetter)
    # when there are no more items in what's being looped through, the code will exit the loop

# the following code—notice it's dedented, outside and after the loop—will only be run once
print('done!')

# we can for-loop through any sequence, for example a list
myList = ['apples', 12.5, 500]
for element in myList:
    print(element)

# and we can loop through a generated sequence like a range
# remember you have to give range() at least one argument, an integer (not a float!)
for num in range(10):
    print(num) # remember the range will start at 0 by default and extend to but not include the integer you give it
    
# let's do something with the loop; we can use the information it generates to draw something over and over on a canvas, but in different positions
newPage()
# let's draw ten evenly-sized vertical stripes over the whole canvas in different shades of grey
for num in range(10):
    # set the fill color using num so that it starts 100% black and ends 100% white
    fill(num/9) # this will be 0/9 = 0 the first time through the loop, and 9/9 = 1 the last time through
    # remember rect() is a DrawBot function that needs four arguments: x and y positions and a width and height
    # width() and height() are DrawBot functions that return the width and height of the active canvas; we want the stripes to be 1/10 the width and the full height of the canvs, and each stripe will be offset by 1/10 of the canvas width
    rect(num * width()/10, 0, width()/10, height())
    
# we can do this with colors too
newPage()
for num in range(10):
    fill(num/9, 0, 0)
    rect(num * width()/10, 0, width()/10, height())

newPage()
for num in range(10):
    fill(1 - num/9, 1, num/9)
    rect(num * width()/10, 0, width()/10, height())

# or why bother with colors in order?
# random() is a Python function that by default returns a decimal fraction from 0 to (not including) 1; it doesn't require arguments to work
newPage()
for num in range(10):
    fill(random(), random(), random())
    rect(num * width()/10, 0, width()/10, height())

# finally let's try something with text
newPage()
myString = 'the quick brown fox'

font('Times') # you can set any installed font
# let's set the font larger than in the previous text sketch
fontSize(130)
# now we'll loop through each character (element) in our string
for myLetter in myString:
    # we'll randomly define two variables for the x and y positions of the letters we'll draw on the canvas
    # randint() is a Python function that takes two arguments: a starting integer and an ending integer; it returns a random integer from between them
    # we'll use width() and height() again, and random() to set the fill = text color
    myX = randint(0, width())
    myY = randint(0, height())
    fill(random(), random(), random())
    # draw our text to the canvas at the random x, y coordinates we just defined
    text(myLetter, (myX, myY))