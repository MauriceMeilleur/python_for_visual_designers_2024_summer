# the default canvas in DrawBot is 1000 x 1000 units
# the 0, 0 origin is at the bottom left of the canvas
# each DrawBot unit = 1 desktop point = 1 pixel

# this code draws a rectangle on the canvas
# rect() is a DrawBot function that takes four arguments: an x-position and a y-position for the lower-left corner of the rectangle, a width, and a height
rect(0, 0, 200, 300)
# this should draw a black rectangle at the lower left corner of the canvas
# when you run a function like rect() that requires an active canvas, DrawBot will create a new default canvas if there isn't one in memory
# the default fill color in DrawBot is 100% black

# let's create a new default canvas
newPage()
# and let's set a new fill color
# fill() is a DrawBot function that sets the color for all subsequent shapes you draw on a canvas (unless you change the color again)
# DrawBot uses an RGBalpha color model by default, and values are mapped onto a decimal fraction 0–1; 0 = 0/255 = 00 = black/(sub)pixel off and 1 = 255/255 = FF = white/(sub)pixel fully on
# fill() takes from 1–4 arguments separated as needed by commas, values 0–1 as above
# 1 argument > greyscale fill
# 2 arguments > greyscale plus alpha (transparency)
# 3 arguments > RGB
# 4 arguments > RGBalpha
# let's set the fill to 100% blue
fill(0, 0, 1)
# and let's draw an oval; oval() is similar to rect(), but you're defining and positioning the bounding box of the shape
oval(0, 0, 300, 300)
# to draw a circle you make the width and height the same
# objects are drawn in the order of the code
fill(0, 1, 0)
rect(150, 150, 300, 300)
# you should see a green square over a blue circle

newPage()
# with each new page DrawBot reverts to its defaults
rect(150, 150, 300, 300)
fill(0, 0, 1)
oval(0, 0, 300, 300)
# now you'll see a blue circle over a black square