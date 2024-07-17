# 18_pvd_skew

# skew() is a DrawBot function that shears the coordinates of the canvas; it takes at least one argument, an angle in degrees
# one angle is for the x-axis; two for the x and y (you can enter 0 for x)

newPage()
fill(1, 0, 0)
skew(45) #positive angle will move coordinates above y = 0 to the right
rect(0, 0, 500, 500)

# again the skew will happen relative to where the code thinks the origin is
newPage()
fill(1, 0, 0)
translate(0, 250)
skew(45)
rect(0, 0, 500, 500)
fill(0, 0, 1)
rect(0, -250, 500, 500)

newPage()
translate(width()/2, height()/2)
skew(45, 22.5)
rect(-250, -250, 500, 500)

# and you can add a final argument, a 2-tuple (x, y) to specify the reference point for the skew
newPage()
# note no translate call for this canvas, but we'll specify a reference for the skew that will produce a similar output
skew(45, 22.5, (width()/2, height()/2))
rect(250, 250, 500, 500)