# 29_pvd_textbox

font('Georgia')
fontSize(100)
lineHeight(120)
text('Hello world!\nHello again!', (100, 240)) # text() essentially has the layout functionality of a typewriter

newPage('Letter')
txt = '''The universe (which others call the Library) is composed of an indefinite, perhaps infinite number of hexagonal galleries. In the center of each gallery is a ventilation shaft, bounded by a low railing. From any hexagon one can see the floors above and below—one after another, endlessly. The arrange­ment of the galleries is always the same: Twenty bookshelves, five to each side, line four of the hexagon’s six sides; the height of the bookshelves, floor to ceiling, is hardly greater than the height of a normal librarian. One of the hexagon’s free sides opens onto a narrow sort of vestibule, which in turn opens onto another gallery, identical to the first—identical in fact to all. To the left and right of the vestibule are two tiny compartments. One is for sleeping, upright; the other, for satisfying one’s physical necessities. Through this space, too, there passes a spiral staircase, which winds upward and downward into the remotest distance. In the vestibule there is a mirror, which faithfully duplicates appearances. Men often infer from this mirror that the Library is not infinite—if it were, what need would there be for that illusory replication? I prefer to dream that burnished surfaces are a figura­tion and promise of the infinite … Light is provided by certain spherical fruits that bear the name ‘bulbs’. There are two of these bulbs in each hexa­gon, set crosswise. The light they give is insufficient, and unceasing.
'''
# calling a new canvas resets text context: font, size, etc
font('Georgia')
fontSize(24)
lineHeight(30)
# we'll draw a rectangle the same size and position as the textBox() we're going to draw, to help us understand what we're making
with savedState():
    fill(.875)
    rect(100, 100, 350, 500)
textBox(txt, (100, 100, 350, 500), align='left')
# default alignment (no argument) is left; also right, center, justified
# note that textBox() will draw as much text from the string as it can inside the box's dimensions; it also returns = stores in memory what is left over, which we can see if we enclose the textBox() call in a print() call
# print(textBox(txt, (100, 100, 350, 500)))
# we can also get that material without printing the textBox() (again) by calling textOverflow() with the same arguments
print(textOverflow(txt, (100, 100, 350, 500), align='left'))

# more methods at drawbot.com/content/text/drawingText.html