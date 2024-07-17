# 12_pvd_line_polygon

# line() is a DrawBot function to draw a line on the canvas; it takes two arguments, 2-tuples for the (x, y) of the start and end of the line

fill(None)
stroke(0)
strokeWidth(40)
line((200, 750), (750, 250))

# polygon() draws a shape with any number of vertices, it takes at least two and as many 2-tuples (x, y) as you want for each vertex
stroke(1, 0, 0)
strokeWidth(5) # weight of stroke in units
polygon((50, 200), (150, 550), (550, 575), (600, 250), (300, 50))

# by default DrawBot will close the path of a polygon, but you can leave it open by adding a last argument, a truth-value for close of False
# so you can use polygon() to draw multi-segment lines
stroke(1, 0, 1)
strokeWidth(20)
# lineJoin() is a DrawBot function to style how straight segments of a line meet
lineJoin('round')
# lineCap() styles the terminators of lines
lineCap('square')

polygon((400, 800), (575, 900), (875, 625), (500, 350), (350, 475), close=False)
stroke(0, 0, 1); strokeWidth(5); fill(0, .125)
polygon((400, 800), (575, 900), (875, 625), (500, 350), (350, 475))
