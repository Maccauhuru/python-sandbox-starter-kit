# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""
print("---------------------------")
print("ASSIGNMENT AND PRINT")
print("---------------------------")


v = 12
v + 10
print(v)


print("---------------------------")
print("SINGLE ASSIGNMENTS")
print("---------------------------")

fl = 3.34  # float
name = "Simba"  # str
isRich = False  # bool
print(fl, name, isRich)

print("---------------------------")
print("MULTIPLE ASSIGNMENTS")
print("---------------------------")

fl, name, isRich = (3.3455, "Michael", True)
print(fl, name, isRich)

print("---------------------------")
print("FIND DATA TYPE")
print("---------------------------")

print(type(name))  # check type
print(type(isRich))  # check type

print("---------------------------")
print("TYPE CASTING")
print("---------------------------")
print("So its " + str(isRich) + " that " + name + " is rich?")
num = float(3) + 12
print(num)
print(type(num))
print(int(num))
