# 39_pvd_spin_chessboard_twophase

canvas = 1080
num = 8
side = canvas/num
off = side
nFrames = 120
fps = 60
phases = 2
# the animation will have two phases of 60 frames each

for phase in range(phases):
    for n in range(nFrames):
        newPage(canvas, canvas)
        frameDuration(1/fps)
        rot = n * 90/nFrames
        # the code will draw black squares over a white background in the first phase, then white over black in the second phase
        if phase == 0:
            fill(1); rect(0, 0, width(), height()); fill(0)
        else:
            rect(0, 0, width(), height()); fill(1)
        translate(width()/2, height()/2)
        translate(-(num - 1) * off/2, (num - 1) * off/2)
        for row in range(num):
            with savedState():
                translate(0, -row * off)
                for col in range(num):
                    with savedState():
                        translate(col * off, 0)
                        if phase == 0: # if we're in the first phase, draw black squares when row + col is odd
                            if (row + col) % 2: # another way of coding 'if (row + col) % 2 == 1:'
                                rotate(rot)
                                rect(-side/2, -side/2, side, side)
                        else: # if we're in the second phase, draw white squares when row + col is even
                            if (row + col) % 2 == 0:
                                rotate(rot)
                                rect(-side/2, -side/2, side, side)

saveImage('spin_chessboard.mp4')