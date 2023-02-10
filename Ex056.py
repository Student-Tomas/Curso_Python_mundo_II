# Challenge number 056: create a code that reads the name, age and gender of four people and, at the end, shows the average age of the group,
# how many women are less than 20 and what is the name of the oldest man.
sum_age = 0
for person in range(1, 5):
    print('----- PERSON NUMBER {} -----'.format(person))
    name = str(input('Name: ')).strip().upper()
    age = int(input('Age: '))
    gender = str(input('Gender: ')).strip().upper()
    sum_age += age
    if gender == 'M' or gender == 'W':
        print("\033[31mLet's go to the next person.\033[m")
    else:
        print('\033[31mGender option invalid! Please, choose only M or W.\033[m')
print(f'The group average age is {sum_age / 4}')
