# strings include characters, not just alphanumeric and punctuation etc but also hidden/non-visible characters like spaces, tabs, and line breaks
# we'll define a variable and give it the value of a string that's a list of all our names, in no particular order, broken by hard returns
# we're manually entering the list in the code, and we don't want the computer to read each new line as if it's a new line of code, so instead of using a single set of quotes to mark the string '' or "", we'll bracket the string with triple quotes
ourNames = '''Courtney
Elizabeth
Alison
JingChing
Sophia
Chag Chag
Kelli
Cameron
Cat
Daniel
Leah
Janine
Maurice
Zrinka
Mika'''
# this looks and prints like a list
print(ourNames)
# but in memory it's just one long string; see what happens when we try to print what looks like the first element in our list
print(ourNames[0])

# so let's redfine ourNames into a Python list object; we'll use the method (only for strings) split()
# we have to give split() an argument, namely on what we want the code to split the list—here we'll tell it to split the list at each hard return; the string '\n' is an expression for the invisible character 'new line'
ourNames = ourNames.split('\n')
# now print ourNames again; now it's a list of strings, one for each name
print(ourNames)
print(ourNames[0])

# shuffle is a Python random function that gets installed with DrawBot; it randomizes the order of a sequence, like a list
shuffle(ourNames)
print(ourNames)
