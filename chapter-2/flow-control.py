# Python flow control using booleans, comparison operators, conditional statements and loops.

# Boolean values
eggs = True         # Evaluates to True
spam = False        # Evaluates to False

# Boolean Operators (and, or, not)
print(eggs and eggs)    # Prints True
print(eggs and spam)    # Prints False
print(spam and spam)    # Prints False

print(eggs or eggs)     # Prints True
print(eggs or spam)     # Prints True
print(spam or spam)     # Prints False

print(not eggs)         # Prints False
print(not spam)         # Prints True

# Comparison operators
print(11 == 11)         # Prints True
print(34 == 23)         # Prints False

print(2 != 4)           # Prints True
print(2 != 2)           # Prints False

print(56 > 10)          # Prints True
print(53 > 61)          # Prints False

print(23 < 40)          # Prints True
print(49 < 1223)        # Prints False

print(123 >= 31)        # Prints True
print(123 >= 123)       # Prints True
print(59 >= 10)         # Prints False
# Same for <=