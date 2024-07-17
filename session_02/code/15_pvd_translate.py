# 15_pvd_translate

# DrawBot can use 'Euclidean transformations' to change the canvas on which you're drawing
# you can also apply these transformations to specific paths you're drawing, but we'll look at them in the context of the canvas first

newPage()
fill(1, 0, 0) # set the fill color to red
rect(0, 0, 150, 150)
# translate() is a DrawBot function that moves the origin point of the canvas; it takes 2 arguments, for the distance to move the origin on the x and y axes
translate(150, 150)
# this is exactly the same code as above, but now run in a context where the origin of the canvas is in a different place
rect(0, 0, 150, 150)