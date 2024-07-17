# 17_pvd_scale

# scale() is a DrawBot function that changes the size of the virtual coordinate grid on the canvas
# scale() takes at least one argument, a float for the scale factor; one argument is understood to scale the canvas by the same factor along both the x and y axes, two arguments to scale it by one factor x and the second y
# again, by default the change happens relative to where the code understands the origin of the canvas to be

newPage()
fill(1, 0, 0)
rect(0, 0, 500, 500)
scale(1.5)
fill(None); stroke(0, 1, 0)
rect(0, 0, 500, 500)
# the scaling factor is always relative to what the code understands the current state of the canvas to be …
scale(.5)
stroke(None); fill(0, 0, 1)
rect(0, 0, 500, 500) # … note that the third square isn't .5 * the first square, it's .5 * the *second* square
