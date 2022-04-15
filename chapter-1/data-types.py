# Info on various data types used in Python

# Integers
int1 = -2
int2 = 3

# Floating-point numbers
float1 = 2.4
float2 = -4.87

# Strings
string1 = 'hello'
string2 = 'world!'

# String operations
# Concatenation
new_string = string1 + ' ' + string2    # Evaluates to 'hello world!'
print(new_string)

# String replication
rep_string = string1 * 5                # Evalueates to hellohellohellohellohello
print(rep_string)

# Int to string
print('Today is the ' + str(int2) + 'rd')

# String to int/float
age = '26'
distance = '32.78'

current_year = 2022
birthyear = current_year - int(age) 
print(birthyear)

total_distance = 20.43 + float(distance)
print(total_distance)