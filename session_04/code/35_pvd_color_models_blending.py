# 35_pvd_color_models_blending

newPage(500, 500)
fill(0)
rect(0, 0, 500, 500)
# blendMode is a DrawBot function that sets the blending mode for the canvas; other modes are 'normal', 'multiply', 'screen', 'overlay', 'darken', 'lighten', 'colorDodge', 'colorBurn', 'softLight', 'hardLight', 'difference', 'exclusion', 'hue', 'saturation', 'color', 'luminosity', 'clear', 'copy', 'sourceIn', 'sourceOut', 'sourceAtop', 'destinationOver', 'destinationIn', 'destinationOut', 'destinationAtop', 'xOR', 'plusDarker', 'plusLighter'
blendMode('screen')
fill(1, 0, 0)
oval(100, 100, 200, 200)
fill(0, 1, 0)
oval(200, 100, 200, 200)
fill(0, 0, 1)
oval(150, 200, 200, 200)

newPage()
blendMode('multiply')
# cmykFill changes the color mode on a canvas from RGBalpha to CMYKalpha; it works exactly the way fill() does but it takes a minimum of 4 and a max of 5 arguments, for CMYKalpha
cmykFill(1, 0, 0, 0)
rect(50, 50, 250, 250)
cmykFill(0, 1, 0, 0)
rect(125, 125, 250, 250)
cmykFill(0, 0, 1, 0)
rect(200, 200, 250, 250)