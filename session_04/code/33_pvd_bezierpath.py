# 33_pvd_bezierpath

# a BezierPath() is a DrawBot object that stores the points of a Bezier path; it can be as simple as a single straight line or contain many contours with lots of segments; it allows you to store the path in memory to redraw it multiple times, or to transform it or combine it in different ways with other BezierPath() objects

path = BezierPath()
path.rect(0, 0, 250, 250)

newPage()
drawPath(path)

path.oval(250, 250, 250, 250)
path.line((250, 500), (500, 250))
path.polygon((500, 500), (750, 500), (750, 750), (250, 750))
newPage()
stroke(0); strokeWidth(10)
drawPath(path)

# you can draw text to a path, but unless you're drawing a FormattedString() the formatting has to be included as arguments
newPage()
t = BezierPath()
t.text('Hello world!', (250, 250), font='Georgia', fontSize=100)
drawPath(t)

newPage()
f = FormattedString('Hello again!', font='Verdana', fontSize=125)
t.text(f, (250, 500))
drawPath(t)

# and you can draw text inside a path using it as a textBox()
newPage()
a = BezierPath()
a.text('a', (200, 200), font='Georgia-Bold', fontSize=1000)
drawPath(a)
font('Georgia'); fontSize(6); fill(1)
textBox('abcdefghijklmnopqrstuvwxyz' * 400, a)