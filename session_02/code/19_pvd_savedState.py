# 19_pvd_savedState

# savedState() is a DrawBot function that allows you to 'pop out' of one graphics state into another without changing the previous one(s)
# it helps you make graphics states into something like Las Vegas: what happens in Vegas stays in Vegas

font('Times')
fontSize(100)

# we call savedState() with the Python statement with, which will run the code indented beneath it as an exception to the conditions of the code around it
with savedState(): # everything in the savedState stays in Vegas …
    font('Papyrus')
    fontSize(50)
    translate(200, 100)
    scale(2)
    rotate(22.5)
    # rotate(45, (100, 100))
    fill(1, 0, 0)
    rect(0, 0, 200, 200)
    text('Las Vegas', (250, 50))

rect(0, 0, 200, 200)
text('Not Las Vegas', (250, 50))