# Challenge 059: create an Options Menu. Enter two numbers and say what you want to do with then.
from time import sleep
num1 = int(input("first number: "))
num2 = int(input("Second number: "))
option = 0
while option != 5:
    option = str(input('''
    [1] sum
    [2] multiplication
    [3] greater
    [4] new numbers
    [5] exit
    >>>>>>> What is your option? '''))
    if option == '1':
        operation = num1 + num2
        print("The sum of {} and {} is {}".format(num1, num2, operation))
    elif option == '2':
        operation = num1 * num2
        print("The multiplication of {} and {} is {}".format(num1, num2, operation))
    elif option == '3':
        if num1 > num2:
            greater = num1
            print("Between {} and {} the greater is {}".format(num1, num2, greater))
        elif num1 < num2:
            greater = num2
            print("Between {} and {} the greater is {}".format(num1, num2, greater))
        elif num1 == num2:
            print('The numbers are equal')
    elif option == '4':
        print('Choose new numbers:')
        num1 = int(input("first number: "))
        num2 = int(input("Second number: "))
    elif option == '5':
        print('Wait ...')
        sleep(4)
        print('Program finished.')
    elif option not in "12345":
        print('Invalid option. Please, choose a valid option.')
    else:
        print()
