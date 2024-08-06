# 42_pvd_quadratic_curve

pts = [(150, 150), (50, 500), (200, 850), (850, 800), (950, 450), (800, 200)]

newPage()
path = BezierPath()
# qCurveTo is a DrawBot function that draws a quadratic Bezier curve; you can moveTo() a starting on-curve point and then qCurveTo() an off-curve point and an on-curve point, segment by segment
# if we want smooth curves from segment to segment we have to make sure that each group of pts off-curve/on-curve/off-curve is collinear
path.moveTo((150, 150))
path.qCurveTo((50, 500), (200, 850))
path.qCurveTo((850, 800), (950, 450))
path.qCurveTo((800, 200), (150, 150))
drawPath(path)

# you can also give it an arbitary list of off-curve points and a final argument, None, which will tell it to interpolate *all* the on-curve points
newPage()
path = BezierPath()
path.qCurveTo(*pts, None)
drawPath(path)