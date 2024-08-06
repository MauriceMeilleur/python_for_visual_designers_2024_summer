# 37_pvd_animation_move

nFrames = 60
fps = 60

side = 500
startX = -side
stopX = width()

for n in range(nFrames):
    newPage()
    frameDuration(1/fps)
    t = n/nFrames # will be a float between 0 and (nFrames - 1)/nFrames
    # lerp is a DrawBot function that interpolates between two numbers; it takes 3 arguments: start, stop, and a float (1.0 = 100%)
    rect(lerp(startX, stopX, t), 250, side, side)
    
saveImage('move_square.mp4')