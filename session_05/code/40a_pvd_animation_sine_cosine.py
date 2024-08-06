# 40a_pvd_animation_sine_cosine

r = width()/4
rT = r * 1.1
nFrames = 360
fps = 6

for n in range(nFrames):
    newPage()
    frameDuration(1/fps)
    translate(width()/2, height()/2)
    th = radians(n)
    fill(None); stroke(1, 0, 0)
    path = BezierPath()
    path.arc((0, 0), r, n, 360, clockwise=False)
    drawPath(path)
    stroke(0, 0, 1)
    path = BezierPath()
    path.arc((0, 0), r, n, 360, clockwise=True)
    drawPath(path)
    polygon((r, 0), (0, 0), (r * cos(th), r * sin(th)), close=False)
    line((-r * 1.5, r), (-r * 1.5, -r))
    line((-r * 1.5 - 5, r * sin(th)), (-r * 1.5 + 5, r * sin(th)))
    line((-r, -r * 1.25), (r, -r * 1.25))
    line((r * cos(th), -r * 1.25 - 5), (r * cos(th), -r * 1.25 + 5))
    stroke(None); fill(0, 0, 1)
    oval(r * cos(th) - 2.5, r * sin(th) - 2.5, 5, 5)
    oval(-2.5, -2.5, 5, 5)
    font('Helvetica'); fontSize(12)
    text('frame count = %s of %s\nΘ = %s°\ncosΘ = %s\nsinΘ = %s\nx = radius × %s\ny = radius × %s' %(
        n,
        nFrames,
        round(degrees(th), 3),
        round(cos(th), 5),
        round(sin(th), 5),
        round(cos(th), 5),
        round(sin(th), 5),), (rT, rT))
    text('0, 0', (r * .025, -r * .05))
    text('x, y', (rT * cos(th), rT * sin(th)))
    text('cosΘ = %s' %round(cos(th), 5), (-r * 1.5 + 7.5, r * sin(th)), baselineShift(-1.5))
    text('sinΘ = %s' %round(sin(th), 5), (r * cos(th), -r * 1.25 - 12))

saveImage('sine_cosine_demo.mp4')