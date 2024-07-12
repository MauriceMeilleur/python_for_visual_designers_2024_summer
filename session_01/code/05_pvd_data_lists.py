# a list is a kind of data object in Python that holds information in a sequence separated by commas, indicated by square brackets
# you can put any kind of data in a list
myList = ['red', 'green', 'blue']
anotherList = [123, 456.0, -123, 'abc']
numberList = [13, 1, 11, 3, 7, 5, 17]

# you can use the len() function on lists
print(len(myList))
# and turn that length into a range
print(range(len(myList)))

# the elements in lists have indices, just like the chatracters in strings
print(anotherList[0])
print(myList[-1])

# but you can replace elements in a list with something else by assigning a new element at the index where you want it
anotherList[2] = 999
print(anotherList)

# you can delete elements in a list
del anotherList[1]
print(anotherList)

# you can append() an element to a list, which puts the new element at the end
numberList.append(19)
print(numberList)
# and you can insert elements into a list; the function needs two arguments: what index to insert the element at, and what the element is—here, insert at index 1 the integer 2
numberList.insert(1, 2)
print(numberList)

# you can sort lists; sorted() is a Python function that returns a sorted version of a list; the list remains unchanged in memory
# A–Z comes before a–z, by the way
print(sorted(numberList))
print(numberList)
print(sorted(myList))
print(myList)
# you can also use a method that *changes* the list in memory, sort()
numberList.sort()
print(numberList)

# let's create a list of strings
myGroceryList = ['apples', 'oranges', 'bananas']
# and get its length; we can include other material to print in a print function call, for example a string to use as a label
print('length:', len(myGroceryList))

# not only can we get a particular element from a list
print('third item:', myGroceryList[2])
# but we can also slice a section of the list; [:2] will give us the first two elements from the list; think of ':' as meaning 'up to', not 'up to and including'
print('first two items:', myGroceryList[:2])
# [-2:] will give us the last two elements from the list
print('last two items:', myGroceryList[-2:])