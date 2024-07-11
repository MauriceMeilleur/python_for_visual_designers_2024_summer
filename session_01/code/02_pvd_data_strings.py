# a string is a data object that contains elements called characters; it can include numerals, punctuation, spaces, and non-printing/invisible characters like line breaks
# strings also belong to the kind of data object Python calls an 'iterable', meaning something that can be counted through 
# Python recognizes strings by seeing their elements inside open/close quotes; you can use single or double quotes, but they have to be paired
myString = 'Hello world!'
print(myString)

# the character elements in a string have positions called indices; the first index is 0, the second is 1, etc. all the way to the last, which is the length of the string minus 1
# strings have lengths you can find by using the Python function len() and passing it the name of the string as an argument
print(len(myString))
# you can single out elements by referring to their index inside square brackets
print(myString[0])
print(myString[3])
print(myString[11])
# you can also call the index of the last element in any string [-1]
print(myString[-1])

# a numeral inside a string isn't a value, it's a character
anotherString = '8'
# if I do math with values, I get meaningful results
print(8/4) # >>2.0
# but not so with strings
print(anotherString/4) # >>error