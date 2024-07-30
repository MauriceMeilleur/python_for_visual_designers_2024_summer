# 31_pvd_textbox_multipage

# code uses DrawBot integration with Mac OS
# drag and drop filepath into the coding window
f = open('borges_library_babel.txt', encoding = 'utf-8') # this opens a file on my desktop …
txt = f.read() # … reads the content …
f.close() # … and closes the file; while a file is open it is locked for editing—best practice is to keep a file open only as long as you need it

print(txt)

margin = 50

# while is a Python function that creates a loop, like for; but instead of looping through a defined sequence a defined number of times, while will loop as long as a defined set of conditions obtains—in this case, as long as the string txt isn't empty
while txt:
    newPage('A5')
    myBox = (margin, margin, width() - margin * 2, height() - margin * 2)
    fill(.9)
    rect(*myBox)
    font('Georgia')
    fontSize(12)
    lineHeight(15)
    fill(0)
    # each time the code redefines the string txt as what is leftover after putting as much of it into the textBox() drawing in the loop
    txt = textBox(txt, myBox, align='left')
    # eventually as we keep creating pages and drawing text on them, we will run out of leftover text; then txt will get redefined as an empty string, and the condition allowing the while loop to continue will no longer obtain, so the loop will end