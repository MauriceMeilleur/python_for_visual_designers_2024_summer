# 32_pvd_formattedstring

# a FormattedString() is a DrawBot object for text with its own formatting that can be drawn as text() or in a textBox(); it needs at least one argument, a string, and optionally takes many different arguments that need to be assigned with labels, many of which also work in DrawBot as global setting
txt = FormattedString('hello', font='Georgia', fontSize=100, fill=(1, 0, 0))
text(txt, (100, 100))

# we can add new blocks of independently formatted text to a FormattedString() using append()
txt.append('world', font='Verdana', fontSize=150, fill=(0, 0, 1)
)
# and draw the object on the canvas using text()
text(txt, (200, 200))

txt.append('!', font='Times', fontSize=250, fill=(0, 1, 0))
text(txt, (100, 300))

# we can also draw the FormattedString() inside a textBox()
newPage()
# note that newPage() doesn't 'reset' any of the formatting in txt, because it carries its own formatting
textBox(txt, (100, 100, 800, 800))

# we can apply OpenType features and adjust OTVar axes to text in a FormattedString()
# there are DrawBot functions to get information about both from a font
print(listOpenTypeFeatures('MinionPro-Regular'))
varFont = '/Users/meilleur/Desktop/cooper/2024_summer/04_code/Recursive_VF_1.077.ttf'
print(listFontVariations(varFont))

# we'll redefine our FormattedString with the content of another external text file 
f = open('/Users/meilleur/Desktop/cooper/2024_summer/04_code/judt_postwar.txt', encoding='utf-8')
t = (f.read())
f.close()

newPage('A5')
txt = FormattedString(t, font='MinionPro-Regular', fontSize=12, lineHeight=15, align='left', firstLineIndent=12, openTypeFeatures={'onum': True, 'smcp': False}) # try setting onum to False and smcp to True
box = (36, 36, width() - 72, height() - 72)
hyphenation(True)
textBox(txt, box)

newPage('A5')
txt = FormattedString(t, font=varFont, fontSize=12, lineHeight=15, align='left', firstLineIndent=12, fontVariations={'slnt': 0, 'CRSV': .5}) # try changing the value of slnt between 0 and -15, and CRSV between 0 and 1
box = (36, 36, width() - 72, height() - 72)
hyphenation(True)
textBox(txt, box)
