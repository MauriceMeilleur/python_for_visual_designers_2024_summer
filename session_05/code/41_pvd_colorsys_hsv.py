# 41_pvd_colorsys_hsv

# this is a library that has code for different models of color and functions to convert them
import colorsys

nFrames = 360
fps = 1/30
canvas = 720

for n in range(nFrames):
    newPage(canvas, canvas)
    frameDuration(fps)
    # HSV stands for hue/saturation/value; it's useful for us in animation if we're making a loop, because hue is defined by degrees on a circle and can be cycled through the same way (the hue at 360º is the hue at 0º); in colorsys calling an HSV color takes three arguments, a float for hue and two floats 0–1 for saturation and value
    # we just want to change the color, so we'll use the frame count to define a float for that argument
    color = n * (360/nFrames)/360
    # color = .5 + sin(n * (2 * pi)/nFrames) * .1
    # now we'll call the colorsys function hsv_to_rgb and give it the HSV definition; it returns three floats 0–1 for the red, green, and blue model equivalent
    r, g, b = colorsys.hsv_to_rgb(color, 1, 1)
    # which we'll use to set the fill()
    fill(r, g, b)
    rect(0, 0, width(), height())
    # the resulting animation will cycle through colors from red around to red seamlessly, which you can't do with RGB numbers directly
    
saveImage('~/Desktop/hsv_color_cycle.mp4')