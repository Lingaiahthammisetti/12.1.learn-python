# This is a single line comment

"""
this is a multi-line comment
"""

# Define a variable
a = 42 # This is a integer variable
print(a) #output:42
# Float value
b = 42.345
print(b) #output:42.345
# Boolean
c = True 
print(c) #output:True

# Strings
d = 'This is a string'
e = "This is also a string"
f = """
This is a multi line string
"""
print(d) #output:This is a string
print(e) #output:This is also a string
print(f) #output:This is a multi line string


# Today's weather is nice
d = 'Today\'s weather is nice'
print(d) #output: Today's weather is nice

d = "Today's weather is nice"
print(d) #output: Today's weather is nice

# This is a list
test_list = ["hello", "world", "python"]
print(test_list) #output: ['hello', 'world', 'python']

# Tuple
test_tuple = ("hello", "world", "python")
print(test_tuple) #output: ('hello', 'world', 'python')

# Dict
test_dict = {'a': 1, 'b': 2}
print(test_dict) #output: {'a': 1, 'b': 2}

# Set
# consider the values in an arbitrary way
test_set = {'a', 'b', "abc"}
print(test_set)  #output: {'abc', 'a', 'b'}

# type() function -> prints the datatype of the variable
print(type(test_dict))  #output: <class 'dict'>
print(type(print))      #output: <class 'builtin_function_or_method'>


# Operations
# Add
# Sub
# Multi
# Divide
# Integer division
# Modulo division

# Add
a = 42
b = 45.32
c = a + b
print(c) #output: 87.32

d = a - b
print(d) #output: -3.3200000000000003

e = a * b
print(e) #output: 1903.44

f = 12
g = 3
h = f / g
print(h, type(h)) #output:4.0 <class 'float'>

# Integer division
h = f // g 
print(h) #output: 4

# Modulo division
i = f % g
print(i) #output: 0

# Addition
a = "42"
b = "43"
print(a + b) #output: 4243

# Power
a = 10
print(a**2) #output: 100

# Comparison operators
a = 10
b = 20
res = a > b
res_1 = a < b
res_2 = a != b
res_3 = a == b
print(res, res_1, res_2, res_3) #output:False True True False

# Logical operators
# AND, NOT, OR
a = True
b = False

res = a and b
res_1 = a or b
res_2 = not a
res_3 = not b
print(res, res_1, res_2, res_3) #output:False True False True
