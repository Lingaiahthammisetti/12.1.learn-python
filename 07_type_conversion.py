sample_str = "This is a sample string"
sample_str_list = list(sample_str)
print(sample_str_list) #output: ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 'a', 'm', 'p', 'l', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']

sample_str_tuple = tuple(sample_str)
print(sample_str_tuple) #output: ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 'a', 'm', 'p', 'l', 'e', ' ', 's', 't', 'r', 'i', 'n', 'g']

split_input = "10 100 200 500 700".split(" ")
print(split_input) #output: ['10', '100', '200', '500', '700']


# Accept input from a user
#user_input = input("Enter a number:")
#print(user_input, type(user_input))

# add_10 = int(user_input) + 10
# print(add_10)

"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/07_type_conversion.py", line 12, in <module>    add_10 = int(user_input) + 10
ValueError: invalid literal for int() with base 10: '10 100 200 500 700'
"""
