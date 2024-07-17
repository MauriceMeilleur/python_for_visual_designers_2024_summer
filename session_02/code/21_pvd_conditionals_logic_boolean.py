# 21_pvd_conditionals_logic_boolean

a = 7
b = 6

# logical operators are used to create statements that can be 'evaluated' by the code
# Boolean values are True/False; when the code evaluates a statement it returns a Boolean value (that we can print, for example)
print(a == b, a != b, a > b, a < b)
print(a >= b, a <= b)

# conditionals: we can use logical statements in if-else tests to decide whether certain lines of code will be run or not
if a > b: # there is always exactly 1 'if'
    print('a is greater than b')
elif a < b: # there can be any number of 'elif's, including none
    print('a is less than b')
else: # there can be at most one 'else'
    print('a is equal to b')
    
# we can evaluate statements about other objects too
c = [1, 2, 3]
print(len(c) > 0)
if c:
    print('the length of c is greater than zero')
d = 1
if d:
    print('the value of d is greater than zero, so d evaluates True')
else:
    print('the value of d is zero, so d evaluates False')
