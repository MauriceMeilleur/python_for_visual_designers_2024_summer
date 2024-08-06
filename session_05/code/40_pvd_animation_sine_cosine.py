# 40_pvd_animation_sine_cosine

size = 100
radius = 300
nFrames = 360
fps = 60

for n in range(nFrames):
    newPage()
    frameDuration(1/fps)
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    # trig functions in Python work with radians, not degrees
    # this line of code translates the frame count into a float that moves between 1 and -1 and back to 1
    r1 = cos(n * (2 * pi)/nFrames) # 2 * pi radians = 360º
    # this line of code translates the frame count into an angle in radians from 0 to just short of 2 * pi (= 360º)
    r2 = n * (2 * pi)/nFrames
    translate(width()/2, height()/2)
    # this square is centered on the origin and will spin around it
    with savedState():
        rotate(r1 * 360)
        rect(-size/2, -size/2, size, size)
    # this triangle is centered on y = 0 and x = radius * cos(r2), it will oscillate sideways between r2 and -r2
    with savedState():
        translate(r1 * radius, 0)
        h = sqrt(3)/2 * size
        polygon((-size/2, -h/3), (0, (2 * h)/3), (size/2, -h/3))
    # this square is centered on the origin and will spin around it counterclockwise 360º, then spin clockwise 360º
    with savedState():
        fill(1)
        rotate(degrees(r2))
        rect(-size/4, -size/4, size/2, size/2)
    # this circle will orbit the origin counterclockwise
    oval(-size/2 + radius * cos(r2), -size/2 + radius * sin(r2), size, size)
    
saveImage('~/Desktop/sine_cosine.mp4')