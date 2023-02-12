# Challenge 085: guessing game
import random
print('I am your PC and I have just chosen a number between 0 and 10.\nDo you think you can guess it?')
PC_number = random.randint(0, 10)
user_number = int(input("Choose a number between 0 and 10: "))
attempts = 1
while PC_number != user_number:
    attempts += 1
    if PC_number > user_number:
        user_number = int(input('Try a bigger one: '))
    if PC_number < user_number:
        user_number = int(input('Try a smaller one: '))
print('Finally! After {} attempts you guessed it.'.format(attempts))


