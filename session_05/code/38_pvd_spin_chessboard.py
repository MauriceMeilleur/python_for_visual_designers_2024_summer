# 38_pvd_spin_chessboard

canvas = 1080
num = 8
side = canvas/num
off = side
nFrames = 120
fps = 60

# if you want to slide squares to the side as they spin
# num += 4 

for n in range(nFrames):
    newPage(canvas, canvas)
    frameDuration(1/fps)
    rot = n * 90/nFrames # why 90º?
    # print(side * 2, n/nFrames * (side * 2), 1/nFrames * (side * 2))
    fill(1); rect(0, 0, width(), height())
    fill(0)
    translate(width()/2, height()/2)
    translate(-(num - 1) * off/2, (num - 1) * off/2)
    for row in range(num):
        with savedState():
            translate(0, -row * off)
            for col in range(num):
                with savedState():
                    translate(col * off, 0)
                    if (row + col) % 2:
                        # translate(lerp(0, side * 2, n/nFrames), 0)
                        rotate(rot)
                        # rotate(rot + (row + col) * 5)
                        rect(-side/2, -side/2, side, side)

saveImage('spin_chessboard.mp4')