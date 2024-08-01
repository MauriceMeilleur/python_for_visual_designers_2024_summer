# pvd_schrofer_illegible_raster

# first we need to import a library of Python code not automatically loaded in DrawBot, one that has functions for 'regular expressions'; we're going to use a combination of them to adjust the text we'll be using to make the 'pixels' in our image
import re

# choose a square image; it can be b/w or color and any size, but the larger the better; the code will output an image of the same dimensions as the original
# drag your image into the coding window to replace the string with the path and filename below
imagePath = '/Users/meilleur/Desktop/cooper/2024_summer/04_code/henri.png'

w, h = imageSize(imagePath)
# this will load the font we'll be using for this sketch; drag the variable font I shared with you into the coding window to replace the string with the path and filename below
f = '/Users/meilleur/Desktop/cooper/2024_summer/04_code/schrofer_05_illegible.ttf'
# now we're going to use the DrawBot function listFontVariations() to get information about the minimum and maximum values for the 'wght' variable axis of the font, assigning each value to its own variable we'll use in the code below 
min_w = listFontVariations(f)['wght']['minValue']
max_w = listFontVariations(f)['wght']['maxValue']

# this will be the pixel resolution of the output image
num = 60
# this defines the size of the pixels
s = w/num

# this is a function that uses methods from the 're' library to strip everything (including white space) out of a string except for alphanumeric characters, then converts all the alphabetic characters to lowercase 
def strip(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

# this is a function that draws the pixels of the output image; it uses the DrawBot function imagePixelColor to sample the color of an image a given number of times in a grid (res) around a given location (loc) (x, y) in the image, calculates an average grey value, then creates a FormattedString() with a given glyph (char) from a variable font set at a given size (size) and with its weight axis set to a value that corresponds to the grey value of the sampled area and draws the FormattedString() as text on the canvas centered on the appropriate location 
def drawWeightedPixel(loc, size, res, char):
    # calculates the spacing of the locations in the sampling grid from each other 
    offset = size/(res)
    # positions the initial sampling spot in the upper left cell of the sampling grid based on the size of the area to be sampled at the given resolution
    tempX = loc[0] - (res - 1) * offset/2
    tempY = loc[1] + (res - 1) * offset/2
    # sets up an temporary 3-element list to sum RGB values for each sample in the grid
    temp = [0, 0, 0]
    for i in range(res):
        y = tempY - i * offset
        for j in range(res):
            x = tempX + j * offset
            #imagePixelColor returns 4 values, each a float from 0–1, but we're only interested in the RGB values, so we'll only put the values at indices 0–2 into color
            color = imagePixelColor(imagePath, (x, y))[:3]
            # adds the sampled values in color to the appropriate tallies in temp
            temp = [temp[n] + color[n] for n in range(len(color))]
    # … and when all the samples are logged for each location in the sampling grid, we divide each tally by the total number of samples to get an average for each value, RGB
    temp = [t/(res ** 2) for t in temp]
    # now we have to convert the RGB values to a grey value, also a float 0–1; we do this by getting their average
    c = sum(temp)/3
    # now we have to turn this grey value into something we can use to adjust the weight axis of the font; we need to invert the value because grey values are 0 (black) to 1 (white), but the weight axis values will run low/light to high/heavy
    c = 1 - c
    # … and now we'll map that value onto the a value between the minimum and maximum 'wght' axis values we read above
    c = min_w + (c * max_w)
    # finally, we'll create a FormattedString() for our grey 'pixel'; it will use the glyph we send it when we call the function and format it with the right size, fill color, and value for the weight axis to make it a darker or lighter 'pixel'
    t = FormattedString(char, font=f, fontSize=size, fill=(0), align='left', lineHeight=size, fontVariations={'wght': c})
    # now we'll draw that pixel on the canvas in the right location using the FormattedString() we made; it includes a correction for the descender value in the variable font to align the cell properly
    text(t, (loc[0] - size/2, loc[1] - size/2 + s/6))


# now we're going to get the content of a text file to use for the 'pixels'; drag the borges_library_babel.txt file into the coding window to replace the string with the path and filename below    
t = open('/Users/meilleur/Desktop/cooper/2024_summer/04_code/borges_library_babel.txt', encoding = 'utf-8')
content = t.read()
t.close()
content = strip(content)
# make sure there's enough text in the stripped string for all the rasterized image 'pixels'; if this test fails the code will stop and throw an error
assert len(content) >= num ** 2


# here's where the main body of the code starts
newPage(w, h)
fill(1)
rect(0, 0, width(), height())

# defines the starting position for sampling the image and drawing the pixels 
startX = s/2; startY = height() - s/2
# each pixel will draw one character at a time from the string variable 'content'; we'll need a counter to keep track of which character to use
count = 0
for row in range(num):
    y = startY - row * s
    for col in range(num):
        x = startX + col * s
        # we'll call the drawWeightedPixel function with the arguments for sampling location (x, y), the size of the pixel, the sampling resolution n inside each cell, and the character for the pixel
        drawWeightedPixel((x, y), s, 3, content[count])
        # we have to increase the counter by 1 each time we draw a pixel so the next pixel uses the next character in the string
        count += 1
        
# saveImage('~/Desktop/pvd_schrofer_illegible_raster.png')
