numberSprinkles = 600

p = BezierPath()
q = BezierPath()
p.oval(250, 250, 500, 500)
q.oval(400, 400, 200, 200)
p = p.difference(q)

newPage()
fill(88/255, 57/255, 39/255)    
drawPath(p)

clipPath(p)
for sprinkle in range(numberSprinkles):
    (x, y) = (randint(250, 750), randint(250, 750))
    fill(random(), random(), random(), )
    oval(x - 5, y - 5, 10, 10)
    
saveImage('clip_sprinkled_donut.png')