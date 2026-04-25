# for and while loop used for iteration
list_of_cars = ['maruti','hyundai','mercedez','mazaradi','morris garage']

for car in list_of_cars:
    print(car)


# while loop: repeats a statement or group of statements while a given condition is True.
# it tests the condition before executing the loop

i = 5
while (i > 1):
    if i == 3:
        continue
    else:
        print(i)
        i-=1



while True:
    print('a')
    break