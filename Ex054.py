# Challenge number 054: build a program that reads the birth's year of sevem people and say whether they can drink or not.
from datetime import date
can_drink = 0
canot = 0
for x in range(7):
    birth_year = int(input('Say the year you were born: '))
    today_year = date.today().year
    age = today_year - birth_year
    if age <= 21:
        print('This person is not allowed to drink.')
        canot += 1
    else:
        print('This person can drink freely.')
        can_drink += 1
print("<=>"*20)
print("{} people are allowed to drink and {} are not.".format(can_drink, canot))




