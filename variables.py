# what are variables?
"""variables are containers that can contain any value.
let's take an example of and as we all know that variable means which is not constand and 
can be changed accrodingly"""

name = "ankelete"
# here name is a varible (= is equal operator ) and  it has now the value or an object is ankelete.

# if we want to  get the output of the variable on the console then we can use print function.
# whatever we give to print func it gives the output to the console.
print(name)

# if we talk about technically .
"""
1.it is a symbolic name that acts as a reference or pointer to an object stored in memory.
2. variables in python do not store actual data. they store reference ( memory address) to the 
object where the data resides.
3.
"""

"""Naming rules:
1. variables are case-sensitive. it means if we have two variables like 'age' and 'Age' both 
define different address not same.
"""
age = 234;
Age = 24;
print(age)
print(Age)
"""
2.variables can not be started with any special character or number except (_)
"""
# %ggoa = 25; it will not work
"""
3. we can not assign reserved keywords to variable name.
"""
# for = 'goav'
# while = 23 will not work
"""
4. we should use snake_case, camelCase or PacalCase to make the code more readable.
"""
user_name = 'gorav';
villageName = 'machhra';
StateName = 'uttar pradesh';
print(f"The name of the user is {user_name} and the village is {villageName} and state is {StateName}")

"""
5. we can assign multiple variables in single line.
"""
# x,y,z = 24,23,2
# print(x,y,z)


# a = b = c = "mango"
# print(a)
# print(b)
# print(c)

# fruits = ['mango','apple']; x,y = fruits

# print(y)


"""
variable scope;
1.local variable: created inside a function and can only be used within a function.
2.global varible: created outside of any function and can be used in the prog anywhere.
3.global keyword : To modify a global variable inside a func, you must explictly use
 the 'global' keyword.
"""

"""
Typecasting:
we can change a variables data type or can check the type of data using type() .
"""

a = 243
print(type(a))

# type casting to float
float_of_a = float(a)
print(type(float_of_a))
print(float_of_a)