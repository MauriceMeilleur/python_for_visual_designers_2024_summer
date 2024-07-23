# 26_pvd_image_pixel_sample

imageName = '/Users/meilleur/Desktop/nasa_colorful_aurora.png'
myImage = ImageObject(imageName)

newPage(*myImage.size())
image(myImage, (0, 0))

# we'll use the DrawBot function imagePixelColor() to sample the image at a specific coordinate on the canvas and get the color of the pixel at that coordinate; the function needs two arguments, the path to the image and the coordinates of the sample
# the function returns a 4-tuple RGBalpha
print(imagePixelColor(myImage, (500, 500)))

# now we'll set a fill() using the elements from the 4-tuple that imagePixelColor() returns
coords = (775, 1150)
fill(*imagePixelColor(myImage, coords))
stroke(1)
strokeWidth(5)
rect(*coords, 200, 200)
