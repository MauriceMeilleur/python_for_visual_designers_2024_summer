# 42a_pvd_animation_quadratic_blob

nFrames = 180
fps = 60

pts = [(150, 150), (50, 500), (200, 850), (850, 800), (950, 450), (800, 200)]
# we're going to vary these points for each frame of the animation by rotating them around; let's make a list of random starting angles and directions for each point so they don't move in sync
# this uses a Python function called a 'list comprehension'
randomPhases = [(2 * pi * random(), choice([-1, 1])) for pt in pts]
print(randomPhases)
# and a radius for their motion
rad = 50

# you can also give it an arbitary list of off-curve points and a final argument, None, which will tell it to interpolate *all* the on-curve points

for n in range(nFrames):
    newPage()
    frameDuration(1/fps)
    fill(1); rect(0, 0, width(), height())
    fill(0)
    t = n * (2 * pi)/nFrames # the 'clock' for the animation
    path = BezierPath()
    # now we'll make a temporary list, temp: for each point in pts, we'll add the radius * the cosine of the clock-angle t plus the random start angle and direction +/- to its x value, and the sine of the clock-angle t plus the random start angle and direction +/- to its y-value, to make a new point; as the frames advance the temporary point will rotate around the position of the original point in pts it's calculated from and wind up at the end of the loop almost back where it started, ready for another loop of the animation 
    temp = [(pts[p][0] + rad * cos(t + randomPhases[p][0] * randomPhases[p][1]), pts[p][1] + rad * sin(t + randomPhases[p][0] * randomPhases[p][1])) for p in range(len(pts))]
    # now we have to feed the points from temp to the BezierPath() object as a qCurve
    path.qCurveTo(*temp, None)
    # and draw the path
    drawPath(path)
    
saveImage('animation_quadratic_blob.mp4')