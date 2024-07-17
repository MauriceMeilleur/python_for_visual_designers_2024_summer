# 23_pvd_functions

# let's make a simple function to convert different color model data to RGBalpha for DrawBot; we'll learn a few more advanced things about Python on the way

# in Python we declare a function with the command def, followed by the arguments the function needs or can use, separated by commas and contained in parentheses, and behind a colon

def fill255(color):
    # all the code at this level will only run if the function is called with any arguments the function needs
    assert all(0 <= x <= 255 for x in color) and (1 <= len(color) <= 4)
    # assert is a Python operator that checks for one or more specified conditions that evaluate True/False; in this case we use the Python operator all() to test whether all the values in the sequence we pass fill255 are 0–255, and whether there's at least one and no more than four values—if a condition evaluated by assert evaluates False the code throws an error and stops
    # this isn't strictly necessary for a function but it's a nice kind of thing to add 
    fill(*[x/255 for x in color])
    # four things: first, the function uses a Python operation called a 'list comprehension'—you can use it to make a list based on the values of an existing list—in this case, the list of values we passed to the list as an argument, 'color'
    # second, the function uses math to convert x/255 color data into a decimal fraction that DrawBot can understand for its default RGBalpha color model; it will convert up to a 4-tuple of values from 0 to 255
    # third, the * is a Python operator that unpacks a sequence; fill() in DrawBot takes 1–4 separate values, not a list of values
    # which brings us to the fourth thing, that the function uses the data it produces to call DrawBot's fill() function—functions can call other functions, and they can even call themselves!
    
newPage()
fill255((128, 64, 128, 255))
rect(0, 0, width(), height())

# def fillHex(color):
    # this function will convert a hex color to RGBalpha for DrawBot; it takes as an argument a string of 2, 4, 6, or 8