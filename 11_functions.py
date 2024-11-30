

#****************************************
def sample_func():
    print("This is a sample function")

# Call the function
sample_func()

# #****************************************
def add(num_1, num_2):
    """
    This function performs addition of 2 numbers
    """
    res = num_1 + num_2
    return res

# Call the function
# res = add(1, 2)
res = add(num_2=1, num_1=2)
print(res)

# #****************************************
def add(num_1, num_2, num_3=10):
    """
    This function performs addition of 2 numbers
    """
    res = num_1 + num_2 + num_3
    return res

#Call the function
res = add(1, 2)
res = add(num_2=1, num_1=2)
print(res)

# # One user enters 10 numbers and another user enters 100 numbers. Define your function to handle this situation
# # A: Variable length arguments
# #****************************************
def add(*nums):
    """
    This function performs addition of 2 numbers
    """
    res = sum(nums)
    return res

res = add(1, 2, 4)
print(res)

res = add(1, 2, 4, 5, 6)
print(res)
# #****************************************
def add(num1, num2, *args):
    """
    This function performs addition of 2 numbers
    """
    res = num1 + num2 + sum(args)
    return res

res = add(1, 2, 4, 5)
print(res)

res = add(1, 2, 4, 5, 6)
print(res)
# #****************************************
def add(*args, **kwargs):
    """
    This function performs addition of 2 numbers
    """
    print(args, kwargs)

res = add(1, 2, 4)
print(res)

res = add(1, 2, 4, num1=5, num2=6)
print(res)

def add(*args, **kwargs):
    """
    This function performs addition of 2 numbers
    """
    print(args, kwargs)

res = add(1, 2, 4)
print(res)
print("=========================================")
def myFun(*argv):
    for arg in argv:
        print(arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print("=========================================")
def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

print("=========================================")

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
print("=========================================")
def myFun(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)
# # map
# # filter
# #****************************************
# # Lambda: inline function

add_numbers = lambda num1, num2: num1 + num2
res = add_numbers(1, 2)
print(res)

