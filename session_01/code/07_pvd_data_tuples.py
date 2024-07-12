# some of the functions we'll use call for information like x, y coordinates, and sometimes you'll need to give them in a form like (x, y)
# a sequence of elements inside round brackets/parentheses is actually a single data object in memory, like a list, but it's called a 'tuple'—depending on how many elements it has, you call it a two-tuple, a five-tuple, etc
# the elements in tuples have indices, too
myTuple = (3, 2, 1)
print(myTuple[1])
# and you can create a temporary sorted-list version of them
print(sorted(myTuple))
# but unlike lists, once you create them, you can't change them in memory in any way
del(myTuple[0])
myTuple.sort()