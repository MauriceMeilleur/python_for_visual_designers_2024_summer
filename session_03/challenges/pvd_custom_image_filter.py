# make a custom function that takes one argument, an image to process
def myCustomFilter(processImage):    
    # get the size of the image to process, we will use it to calculate the center
    imageWidth, imageHeight = processImage.size()
    # get the center point of the image
    center = (imageWidth/2, imageHeight/2)
    # invert the colors
    processImage.colorInvert()
    # posterize the image
    processImage.colorPosterize()
    # apply a twirl distortion located at the center which occupies 1/3 of the image
    processImage.twirlDistortion(center, width() * .75)

myImage = ImageObject('image') # your image here
# call the custom effects function with the image as an argument
myCustomFilter(myImage)            
# create a new canvas
newPage(*myImage.size()) 
# draw the image
image(myImage, (0, 0))    

saveImage('custom_filter_function.jpg')