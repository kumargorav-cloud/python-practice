# expception handling: so that the prog can run without any error
# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

try:
    print(x)
except:
    print("an error orrured!")


# using multiple errors
try:
    print(y)
except NameError:
    print("vafiable x is not defined")
except:
    print("something else went wrong")


# using else for when nothing goes wrong
try:
    print(name)
except:
    print("something went wrong")
else:
    print('nothing went wrong')

# finally it executes regardless of what is done

try:
    print(nothing)
except:
    print('something went wrong')
finally:
    print("the 'try except' is done and this is 'finally'")

# lets have some error handling with user input

# number_user = (input("Enter the number:\n"))
# if int(number_user) < 0:
#     raise Exception('No number less then zero')
# elif type(number_user) is int:
#     raise TypeError("Only integers are allowed")
# else:
#     print(number_user)

string = 55
if not type(string) is str:
    raise TypeError("only string is allowed!!")
