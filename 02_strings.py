#sample_str = "This-is-a-sample-string"

sample_str = "Hello-world"
print(sample_str) #output: Hello-world

# How to access individual characters from a string
print(sample_str[8]) #output: r
 
# Slicing
sub_str = sample_str[2:7] 
print(sub_str) #output: llo-w

sub_str = sample_str[:] 
print(sub_str) #output: Hello-world

sub_str = sample_str[1:]  
print(sub_str) #output: ello-world

sub_str = sample_str[:5]
print(sub_str) #output: Hello

sub_str = sample_str[::1] 
print(sub_str) #output: Hello-world

sub_str = sample_str[::2] 
print(sub_str) #output: Hlowrd

sub_str = sample_str[::3] 
print(sub_str) #output: Hlwl

# Reverse a string
sub_str = sample_str[::-1]
print("Reversed string:", sub_str) #output: Reversed string: dlrow-olleH

# Length of a string
len_str = len(sample_str)
print("Length of a string:", len_str) #output:Length of a string: 11

# Method
sample_str = "hello"
print(sample_str.capitalize()) #output: Hello

# split(), join(), format(), count(), strip(), lstrip(), rstrip()
sample_str = "This is a sample string"
str_split = sample_str.split() 
print(str_split, type(str_split)) #output:['This', 'is', 'a', 'sample', 'string'] <class 'list'>

join_split_str = " ".join(str_split)
print(join_split_str, type(join_split_str)) #output: This is a sample string <class 'str'>

count_a = sample_str.count('o')
print(count_a) #output: 2

sample_str = "    devops is a very good career choice   "
strip_str = sample_str.strip()
print(strip_str) #output: devops is a very good career choice

# Strings are immutable
sample_str = "This is a sample string"
sample_str[-1] = 'G'
print(sample_str)

"""
Traceback (most recent call last):
  File "/home/cloudshell-user/python-devops/02_strings.py", line 52, in <module>
    sample_str[-1] = 'G'
TypeError: 'str' object does not support item assignment
"""
