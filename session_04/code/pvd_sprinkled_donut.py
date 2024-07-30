x, y = (500, 500)

p = BezierPath()
q = BezierPath()
p.oval(250, 250, 500, 500)
q.oval(400, 400, 200, 200)
p = p.difference(q)
if p.pointInside((x, y)):
    print('inside!')
else:
    print('outside!')
drawPath(p)
fill(1, 0, 0)
oval(x - 5, y - 5, 10, 10)


numberSprinkles = 500

p = BezierPath()
q = BezierPath()
p.oval(250, 250, 500, 500)
q.oval(400, 400, 200, 200)
p = p.difference(q)

sprinkles = []
for sprinkle in range(numberSprinkles):
    while True:
        (x, y) = (randint(250, 750), randint(250, 750))
        if p.pointInside((x, y)):
            sprinkles.append((x, y))
            break
        
newPage()
fill(88/255, 57/255, 39/255)    
drawPath(p)
for sprinkle in sprinkles:
    x, y = sprinkle
    fill(random(), random(), random(), )
    oval(x - 5, y - 5, 10, 10)
    
saveImage('sprinkled_donut.png')