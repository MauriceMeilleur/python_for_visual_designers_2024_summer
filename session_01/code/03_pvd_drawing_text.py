# let's see what fonts are installed on our machine
# installedFonts() is a DrawBot function that returns a list of the PostScript names of every active installed font it finds on the computer
print(installedFonts())
# lists are data objects that have lengths, like strings, so we can use the Python function len()
print(len(installedFonts()))

# let's set the font we're going to use for drawing text on the canvas choosing from the list
# font() is a DrawBot function that needs at least one argument, the PostScript name of a font as a string
font('Times')
# we'll set the size of the text set in that font in DrawBot units (= dtps, pixels) with the DrawBot function fontSize()
fontSize(50)

# now we're going to draw the text; the DrawBot function text() requires a canvas to work, so DrawBot will create one for us using the default settings
# text() needs two arguments: a string it will use for the text, and DrawBot will set the text in the font we chose at the size we specified, and a location (x, y) to draw it, separated by a comma
text('Hello world!', (100, 100))

# we can pass text() a variable name for the text if it's a string
# because there's an active canvas, DrawBot won't create another one unless/until we tell it to
# the fill() function also controls the color of text drawn with text()
fill(1, 0, 0)
myString = 'Hello again!'
text(myString, (300, 300))

# try changing fonts, font sizes, colors, and positions!
