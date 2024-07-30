import os
import re
from vanilla.dialogs import getFile

# choose a square image 2160px on a side if you want to share; it can be b/w or color
imagePath = '/Users/meilleur/Desktop/cooper/2024_summer/04_code/henri.png'

w, h = imageSize(imagePath)
# this will load the font we'll be using for this sketch
f = '/Users/meilleur/Desktop/cooper/2024_summer/04_code/schrofer_05_illegible.ttf'
num = 60
s = w/num
min_w = listFontVariations(f)['wght']['minValue']
max_w = listFontVariations(f)['wght']['maxValue']

# this is a function that strips everything (including white space) out of a string except for alphanumeric characters, then converts all the letters to lowercase 
def strip(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    
t = open('/Users/meilleur/Desktop/cooper/2024_summer/04_code/borges_library_babel.txt', encoding = 'utf-8')
content = t.read()
content = strip(content)
# make sure there's enough text in the string for the rasterized image 'pixels'
assert len(content) >= num ** 2

# this is a function that uses the DrawBot function imagePixelColor to sample the color of an image a given number of times in a grid (res) around a given location (loc) (x, y), calculates an average grey value, then creates a FormattedString() with a given glyph (char) from a variable font set at a given size (size) and with its weight axis set to a value that corresponds to the grey value of the sampled area and draws the FormattedString as text on the canvas centered on the appropriate location 
def getColorArrayCell(loc, size, res, char):
    off = size/(res)
    # positions the initial sampling spot based on the size of the area to be sampled at the given resolution and filled with a character
    tempX = loc[0] - (res - 1) * off/2
    tempY = loc[1] + (res - 1) * off/2
    # sets up an temporary 3-element list to sum RGB values for each sample; this list will be remade for each sample/call of this function
    temp = [0, 0, 0]
    for i in range(res):
        y = tempY - i * off
        for j in range(res):
            x = tempX + j * off
            color = imagePixelColor(imagePath, (x, y))[:3]
            # adds the sampled values to the appropriate tallies in temp
            #imagePixelColor returns 4 values, each a float from 0–1, but we're only interested in the RGB values; the code below adds each value to the element at the appropriate position in the list
            temp = [temp[n] + color[n] for n in range(len(color))]
    # … and then divides each tally by the total number of samples to get an average for each value, RGBalpha
    temp = [t/(res ** 2) for t in temp]
    # now we have to convert the RGB values to a grey value; we do this by getting their average
    c = sum(temp)/3
    # now we have to turn this grey value 0–1 into something we can use to adjust the weight axis of the font; we need to invert the value because grey values are 0 (black) to 1 (white) but weight axis values are 100 (light) to 900 (heavy)
    c = 1 - c
    # … and now we'll map that value onto a range, 100–900
    c = 100 + (c * 800)
    # … and finally create and draw a FormattedString() for our grey 'pixel'
    t = FormattedString(char, font=f, fontSize=size, fill = (0), align='left', lineHeight=size, fontVariations={'wght': c})
    text(t, (loc[0] - size/2, loc[1] - size/2))

newPage(w, h)
fill(1)
rect(0, 0, width(), height())
translate(0, s/6)

areas = []
startX = s/2; startY = height() - s/2
count = 0
for row in range(num):
    y = startY - row * s
    for col in range(num):
        x = startX + col * s
        getColorArrayCell((x, y), s, 3, content[count])
        count += 1
        
# saveImage('~/Desktop/schrofer_illegible_raster.png')