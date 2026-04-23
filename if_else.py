# if else statements:
# define a voting system
age = 18
while True:
    user_input = int(input("Enter your age:\n"))
    if type(user_input) == str:
        break
    elif user_input <= age:
        print("You are not ready to vote yet.")
    elif user_input > 80:
        print("You are too old to vote.")
    elif user_input == 0:
        break
    else:
        print("You can vote")
    