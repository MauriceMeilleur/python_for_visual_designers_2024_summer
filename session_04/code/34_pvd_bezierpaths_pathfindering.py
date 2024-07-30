# 34_pvd_bezierpaths_pathfindering

a = BezierPath()
b = BezierPath()
c = BezierPath()

a.rect(200, 200, 250, 250)
b.oval(300, 300, 250, 250)
c.rect(400, 400, 250, 250)

fill(None)
stroke(0)

drawPath(a)
drawPath(b)
# drawPath(a.intersection(b))
# drawPath(a.difference(b))
# drawPath(a.union(b))

# fill(0)
# drawPath(b.xor(a))

drawPath(c)
# drawPath(c.difference(a.intersection(b)))
# drawPath(c.union(b.intersection(a)))

# all paths are still in memory; but you can also permanently modify paths by redefining the path with its changes

# you can apply transformations directly to paths
a.translate(300, 300)
# a.scale(1.5)
a.rotate(0, (625, 625))
drawPath(a)

d = a.copy() #need this method to copy to a unique memory object; as with other objects, d = a would just create another reference for the same object
d.translate(0, -300)
drawPath(d)
# drawPath(a)

# the direction of paths and contours matters for how they interact when they overlap
newPage()
fill(1)
rect(0, 0, width(), height())
fill(0)
translate(width()/2, height()/2)
e = BezierPath()
f = BezierPath()
e.rect(-250, -250, 500, 500)
f.rect(34, -110, 200, 200)
f.reverse()
e = e + f

drawPath(e)
# drawPath(f)

newPage()
fill(1)
rect(0, 0, width(), height())
fill(0)
txt1 = 'a'; txt2 = 'b'
g = BezierPath()
h = BezierPath()
g.text(txt1, (200, 200), font='Arial Bold', fontSize=400)
h.text(txt2, (250, 250), font='Arial Bold', fontSize=400)
# h.rotate(90, (300, 300))
h.reverse()
g = g + h
g.rotate(-5)

drawPath(g)
# drawPath(h)