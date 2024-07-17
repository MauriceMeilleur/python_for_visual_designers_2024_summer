# 22_pvd_chessboard

# let's put a bunch of things together now to draw a proper chessboard
# the convention for drawing chessboards in diagrams is to draw with Black at the top and White at the bottom, which means that the upper-left corner square is white

canvas = 1080
num = 8
size = canvas/num
offset = size

newPage(canvas, canvas)
with savedState():
    fill(1) # fill() in its own graphics state
    rect(0, 0, width(), height()) # background color will be white
translate(width()/2, height()/2) # translates the origin of the canvas to its center
translate(-(num - 1) * offset/2, (num - 1) * offset/2) # we'll start drawing squares from the top left; this translates the origin to the center of where the first square on the chessboard will be
for row in range(num):
    with savedState():
        translate(0, -row * offset) # row position will move down the board
        for col in range(num):
            with savedState():
                translate(col * offset, 0) # col position will move left to right
                if (row + col) % 2: # % is the Python modulo operator—it returns the remainder of x/y; for any even integer x, x % 2 = 0, and for odd integers, x % 2 = 1
                    # the Boolean value of 0 is false, and the Boolean value of 1 is True; another way to write this if statement is 'if (row + col) % 2 == 1:' 
                    rect(-size/2, -size/2, size, size)
                    # note that we only need to draw the black squares because the background is already white; and DrawBot's default fill color is black, meaning fill(0)
                    # note also that as far as the code is concerned, each square on the board is centered on the origin (0, 0) because we keep translating to each new position inside savedState() calls