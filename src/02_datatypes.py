"""
Python is a strongly-typed language under the hood, which means 
that the types of values matter, especially when we're trying
to perform operations on them. 

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# Convert str to int
y_int = int(y)

# Perform arithmetic
my_sum = x + y_int
print("The sum of {} and {} is: {}".format(x, y_int, my_sum))


# Write a print statement that combines x + y into the string value 57

# Convert int to str
x_str = str(x)

# concat strings
my_str = x_str + y
print("{} and {} concatenated is: {}".format(x_str, y, my_str))