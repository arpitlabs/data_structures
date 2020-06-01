# Multiline strings start and end with three quotes """
multiline_string = """This is line 1
# This is line 2
# This is line 3"""
print(multiline_string)
print()

# String formatting: use f strings, use {} to put variables"
# Example 1: use f string with variable names surrounded by {}
age = 34
name = "Arpit"
print(f"{name}, you are {age}")
print()

# Example 2: use empty {} and use format method to pass variables. The result has variable values filled in {} in the same  order in which variables are passed in format(<var1>, <var2>)")
message = "{}, {} is great!"
message = message.format(name, age)
print(message)
print()

# Example 3: use a variable in {} and then pass value of variable in format(<variable_name>=\"<value>\"")
message = "How are you, {name}"
print(message.format(name="Sir"))
print()

message = "How are you, {name}"
message = message.format(name=name)
print(message)
print()
