# if else statements:
# define a voting system
# age = 18
# while True:
#     user_input = int(input("Enter your age:\n"))
#     if type(user_input) == str:
#         break
#     elif user_input <= age:
#         print("You are not ready to vote yet.")
#     elif user_input > 80:
#         print("You are too old to vote.")
#     elif user_input == 0:
#         break
#     else:
#         print("You can vote")

# assignments 
# find the number is +ve -ve or 0

# number = int(input("Enter the number you want to check:\n"))

# if number > 0:
#     print("Number is +ve")
# elif number < 0:
#     print("Number is Negative")
# else:
#     print("Number is zero")



#find the odd and even

# odd_even = int(input("Enter the number to check:\n"))
# if odd_even%2==0:
#     print("The number is even")
# elif odd_even <= 2:
#     print("Enter number greater than 2")
# else:
#     print("The number is odd")


# calculator
print("welcome here with the mini calculator !!")
num1 = int(input("Enter the number 1:\n"))
num2 = int(input("Enter the number 2:\n"))
operations =['+','-','*','**','/','%','//']
print(f"select the operation to perform : {operations}")
operations_selection = input()
result = "the result is:"
if operations_selection == '+':
    print(f"{result}{num1+num2}")
elif operations_selection == '-':
    print(f"{result}{num1 - num2}")
elif operations_selection == '*':
    print(f"{result}{num1*num2}")
elif operations_selection == '**':
    print(f"{result}{num1**num2}")
elif operations_selection == '/':
    print(f"{result}{num1/num2}")
elif operations_selection == '%':
    print(f"{result}{num1%num2}")
elif operations_selection == '//':
    print(f"{result}{num1//num2}")
else:
    print("no result found!!")