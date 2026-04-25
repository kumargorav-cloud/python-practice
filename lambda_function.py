# a lambda function is an anonyms function:
# it can take any number of arguments but with a single expression;
# how to write:
# lambda argument(s):expression

sum = lambda a: a+10
print(sum(4))

x = lambda a,b: a * b
print(x(3,2))

y = lambda a , b ,c : a+b+c
print(y(1,2,3))

# why we use it: the power of this fun can be seen when we use it inside any function

# write a prog that doubles the given argument
def double_number(n):
    return lambda a : a * n

my_double = double_number(2)
print(my_double(12))

my_triple = double_number(3)
print(my_triple(10))


# lambda with built in functions
# map():it applies a fun to every item in an iterable
numbers = [1,2,3,4,5]
# map returns a list 
doubled = list(map(lambda a: a*2,numbers))
print(doubled)

# filter():creates a list of items for which a function is true

# finding odd from list

list_get_odd = [2,4,5,6,7,8,9,11]
odd_nums = list(filter(lambda a: a%2!=0,list_get_odd))
print(odd_nums)

# sorted(): a key for custom sorting
# sort a list of tuple by second element
students = [('gorav',22),('aniket',20),('sagar',30)]
sorted_item = sorted(students,key=lambda x:x[1])
print(sorted_item)

# sort string by length words length
words = ['apple','pie','banana','cherry']
sorted_words = sorted(words,key=lambda a : len(a))
print(sorted_words)