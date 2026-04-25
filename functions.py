# functions are used to get rid of repetitive code 
# and it only runs when it is called.
# it can return a data as a result.

def sum(a,b):
    return a+b

# new_sum =  sum(43,4)
# print(new_sum)

print(sum(4235,523))

# arguments are specified inside a function name which can be used to perform any task.
# peremeters are when we define a function
# arguments are when we call a function
def greet(name):
    return f"Hello {name}"

print(greet("gorav"))

# *args and *kwargs
# args : used when we do not know how many parameters can be passed to a function
# it creates a tuple of arguments
# def my_younger_child(*kids):
#     print(f"the younger child is {kids[2]}")

# my_younger_child('aniket','subham','ritika','avinash')

# print("=======================================")
# def my_function(*args):
#     print("Type:",type(args))
#     print("first argument:",args[0])
#     print("second argument:",args[1])
#     print("third argument:",args[2])

# my_function('Rishi','Sunak','Abishek','Ritikash')

# using args with regular arguments
def grettings(gretting,*names):
    for name in names:
        print(gretting,name)

# here hello is regular argument and the other are *args
grettings('Hello','rishi','anklete','anirudh')


# finding the maximum of given numbers
def maximum_number(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(maximum_number(2,4,5,6,234,1))

# return sum of given numbers
def summarization(*numbers):
    if len(numbers) == 0:
        return None
    sum = 0
    for i in numbers:
        sum+=i
    return sum
print(summarization(1,3,4,6,7,2,77,555,45235,23423,55))

# kwargs: it is used when we do not know how many keyword arguments we need to pass.
# inside a function this becomes a dict containing all the keyword arguments.

def new_function(**kwargs):
    print(f"Type: {type(kwargs)}")
    print(f"Name: {kwargs['name']}")
    print(f"Age: {kwargs['age']}")
    print(f"City: {kwargs['city']}")
    print(f"Total data: {kwargs}")


new_function(name="gorav",age=23,city='machhra')

# using with regular arguments
def employee_details(username,**details):
    print("Username:",username)
    print("Additional details")
    print(f"Name:{details['name']} | State:{details['state']} | ID:{details['id']}")

employee_details('goravkumar',name='amit kumar',state='uttar pradesh',id=101)


# combining both args and kwargs
# order 1.regular peremets 2.args 3. kwargs
def args_and_kwargs(title,*args,**kwargs):
    print("Title:",title)
    print("Positional Arguments:",args)
    print("Keyword Arguments:",kwargs)

args_and_kwargs('Information','arg1','arg2',name='kwarg1',name2='kwarg2')

# we can use * and ** when function calling to unpack arguments
def sum(a,b,c):
    return a+b+c

my_list = [1,2,3]
list_sum = sum(*my_list)
print(list_sum)

def details_(title,name,age):
    print(f"Hello {title} your name is {name} and your age is {age}")

person_details = {'title':'given_title','name':'Anirudh','age':22}

details_(**person_details)