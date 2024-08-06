# 36_pvd_animation_spin

nFrames = 60
fps = 60

for n in range(nFrames):
    newPage()
    # frameDuration sets a frame rate for canvases that are saved as frames in a motion format in DrawBot (.gif, .mp4); it needs a canvas for a context so don't call it until you've created the page for your frame
    frameDuration(1/fps)
    rot = n * 90/nFrames # will be a number between 0 and (nFrames - 1) * 90/nFrames
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    translate(width()/2, height()/2) # put the origin in the center of the canvas for the rotation axis
    with savedState():
        rotate(rot)
        rect(-250, -250, 500, 500)
        
saveImage('spin_square.mp4')