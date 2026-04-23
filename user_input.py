# in this we will learn how to get input from the user and how to operate with them.
# when we take input from the user we get the data type string by default.
# number1 = int(input("Enter the number 1:\n"))
# number2 = int(input("Enter the number 2:\n"))
# number3 = input("Enter the number 3:\n")

# # it will reponde with string data type
# print(type(number3))

# print(f"The sum of the number {number1} and number {number2} is : {number2+number1}")

list = []
for fruit in range(1,5):
    fruit_name = input(f"Enter the fruits name {fruit}:\n")
    list.append(fruit_name)

print(list)
