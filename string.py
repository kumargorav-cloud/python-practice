#string : sequence of characters
myString = 'this is my string'
print(f"this string is written in single quotes: {myString}")
myStringDoubleQuotes = " this is double quotes"
print(f"this is double quotes string: {myStringDoubleQuotes}")
multilineString = """
this is multi line 
string and can be written in 
multiple lines
"""
print(f"this is multiple line string : {multilineString}")

# operations with string
#string slicing
string_for_operation = "this is my string and can be used for any type of operations"
sliced_string=string_for_operation[0:15] # it will exclude the latter one
jumped_string = string_for_operation[0:20:2]
revese_string = string_for_operation[::-1]
print(sliced_string)
print(jumped_string)
print(revese_string)
print('used' in string_for_operation)
print(string_for_operation.capitalize())
print(string_for_operation.upper())
print(string_for_operation.casefold())
print(string_for_operation.replace('b','d'))

# returns the list of given string with given condition that where should it split the string.
print(string_for_operation.split(" "))

fruit_list_string = "banana papaya watermelon guava grape orange kiwi"
fruit_list = fruit_list_string.split(" ")
for fruit in fruit_list:
    modified_name = fruit.capitalize()
    print(modified_name)

