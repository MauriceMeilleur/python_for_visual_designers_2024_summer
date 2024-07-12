# there are two kinds of numbers in Python to pay attention to, integers and floats
# integers are whole numbers, the kind of number you'd use to respond to a question like 'how many people are in the room?'
# Python assumes a number without a decimal point is an integer
myInteger = 7

# the other kind of number is called a float (for 'floating-point number')
# that kind of number includes a decimal fraction
myFloat = 7.0

# you can do math with both kinds of number
# add + and subtract -
print(myInteger + myFloat)
print(myInteger - myFloat)
# multiply * and divide /
print(myInteger * myFloat)
print(myInteger/myFloat)
# the result of a math operation with a float is *always* a float

# you can change the value of an existing number variable using +=, -=, *=, /=
# these are examples of what are called 'recursive' operators
myInteger += 7 # means, 'let myInteger equal [the existing] myInteger plus 7'
# in the above line of code is an example of an 'inline comment', by the way
print(myInteger)
myInteger -= 7 # 'let myInteger equal myInteger minus 7'
print(myInteger)
myInteger *= 7 # 'let myInteger equal myInteger times 7'
print(myInteger)
myInteger /= 7 # 'let myInteger equal myInteger divided by 7'
print(myInteger) # division always yields a float

# range() is a Python function that returns a sequence of numbers starting at 0 and continuing until (but not including) a specified number
# it needs at least one argument, an integer at which it stops
print(range(7)) # shows where the sequence starts and stops
# right now in memory, thanks to the last division operation we did, myInteger in memory is actually a float; if we give it as an argument to range(), we'll get an error
print(range(myInteger))
# but we can convert a float to an integer using the Python function int(); comment out the above line and try this code:
myInteger = int(myInteger)
print(range(myInteger))

# and we can convert an integer into a float with float()
myInteger = float(myInteger)
print(myInteger)
