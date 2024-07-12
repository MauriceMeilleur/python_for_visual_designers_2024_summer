# by default DrawBot saves its files with a .py extension to your desktop

# by default it saves output files (images, vectors, video) to the folder where the DrawBot file that generated them is

# here's the code for the crazy chessbard again:
newPage()
sWidth = width()/8
sHeight = height()/8
offset = sWidth
for y in range(8):
    yTemp = y * offset
    for x in range(8):
        xTemp = x * offset
        fill(random(), random(), random())
        rect(xTemp, yTemp, sWidth, sHeight) 

# let's save the image; saveImage() is a DrawBot function that needs at least one argument, a filename in the form of a string
# set the format by adding the proper extension to the filename
saveImage('crazy_chessboard.png')
saveImage('crazy_chessboard.jpg')
saveImage('crazy_chessboard.pdf')
saveImage('crazy_chessboard.gif')
saveImage('crazy_chessboard.svg')
saveImage('crazy_chessboard.bmp')
# DrawBot will overwrite any file with the same name & extension in the location where you're saving
# you can also save the file in any existing folder by adding the folder location; for example, putting the file on the desktop on purpose
saveImage('~/Desktop/crazy_chessboard.png')