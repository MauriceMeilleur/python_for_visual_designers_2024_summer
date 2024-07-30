# 30_pvd_textbox_type_specimen

txt = '''The universe (which others call the Library) is composed of an indefinite, perhaps infinite number of hexagonal galleries. In the center of each gallery is a ventilation shaft, bounded by a low railing. From any hexagon one can see the floors above and below—one after another, endlessly. The arrange­ment of the galleries is always the same: Twenty bookshelves, five to each side, line four of the hexagon’s six sides; the height of the bookshelves, floor to ceiling, is hardly greater than the height of a normal librarian. One of the hexagon’s free sides opens onto a narrow sort of vestibule, which in turn opens onto another gallery, identical to the first—identical in fact to all. To the left and right of the vestibule are two tiny compartments. One is for sleeping, upright; the other, for satisfying one’s physical necessities. Through this space, too, there passes a spiral staircase, which winds upward and downward into the remotest distance. In the vestibule there is a mirror, which faithfully duplicates appearances. Men often infer from this mirror that the Library is not infinite—if it were, what need would there be for that illusory replication? I prefer to dream that burnished surfaces are a figura­tion and promise of the infinite … Light is provided by certain spherical fruits that bear the name ‘bulbs’. There are two of these bulbs in each hexa­gon, set crosswise. The light they give is insufficient, and unceasing.
'''

fontList = installedFonts()
print(len(fontList)) # the number of pages in our specimen

for fontName in fontList:
    newPage('Letter')
    font(fontName)
    fontSize(20)
    # draw a title for each page with the font name
    text(fontName, (100, height() - 100))
    # reset for the body of the specimen
    fontSize(14)
    hyphenation(True)
    # we'll fit the body inside the given page size
    textBox(txt, (100, 100, width() - 200, height() - 300), align = 'left')
    # we'll add a folio at the bottom
    font('Verdana')
    fontSize(10)
    text(str(pageCount()), (100, 50))    
# let's make the same specimen with two columns
margin = 80
gutter = 10
numColumns = 2

for fontName in fontList:
    newPage('Letter')
    font(fontName)
    fontSize(20)
    text(fontName, (margin, height()- 100))
    fontSize(14)
    hyphenation(True)
    # column width will be taken out of what's left over on any size page created after subtracting margins and gutter
    columnWidth = (width() - 2 * margin - gutter * (numColumns - 1)) / numColumns
    columnHeight = height() - 300    
    copy = txt # we need to make a fresh copy of the text for each page because we're going to take the overflow from the first column and drop it in the second column
    for i in range(numColumns):
        x = margin + i * (columnWidth + gutter)
        y = margin
        # here again we'll draw rectangles to help us understand where we're drwing the text boxes
        fill(.9)
        rect(x, y, columnWidth, columnHeight)
        fill(0)
        # we'll redefine the full text in copy with what's leftover after calling and drawing the first textBox()
        copy = textBox(copy, (x, y, columnWidth, columnHeight))
        
    font('Verdana')
    fontSize(10)
    text(str(pageCount()), (margin, margin/2))