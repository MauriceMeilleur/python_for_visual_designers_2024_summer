# 16_pvd_rotate

# rotate() is a Drawbot function that spins the canvas around a specific point; by default that point is whereever the code understands the origin (0, 0) to be

newPage()
fill(1, 0, 0) # set the fill color to red
rect(400, 400, 200, 200)
# rotate() takes at least one argument, the degrees of rotation
# DrawBot understands degrees as follows: 0º = east, 90º = north, 180º = west, 270º = south
# thus positive rotation = counterclockwise, negative = clockwise
rotate(45)
rect(400, 400, 200, 200)

# we can supply a second argument to rotate(), a 2-tuple (x, y) for the axis of rotation
# again that position will be understood in the context of where the code understands the origin of the canvas to be—so if we have moved that origin with transform(), we have to take that into account
newPage()
fill(1, 0, 0)
rect(350, 350, 300, 300)
rotate(45, (500, 500))
fill(0, 0, 1)
rect(350, 350, 300, 300)