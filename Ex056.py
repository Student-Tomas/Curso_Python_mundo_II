# Challenge number 056: create a code that reads the name, age and gender of four people and, at the end, shows the average age of the group,
# how many women are less than 20 and what is the name of the oldest man.
sum_age = 0
oldest_man_age = 0
oldest_man_name = ' '
total_women_20 = 0
for person in range(1, 5):
    print('----- PERSON NUMBER {} -----'.format(person))
    name = str(input('Name: ')).strip().upper()
    age = int(input('Age: '))
    gender = str(input('Gender: ')).strip().upper()
    sum_age += age
    if person == 1 and gender == "M":
        oldest_man_age = age
        oldest_man_name = name
    if gender == "M" and age > oldest_man_age:
        oldest_man_age = age
        oldest_man_name = name
    if gender == "W" and age < 20:
        total_women_20 += 1
    if gender == "M" or gender == 'W':
        print("\033[31mLet's go to the next person.\033[m")
    else:
        print('\033[31mGender option invalid! Please, choose only M or W.\033[m')
print(f'The group average age is {sum_age / 4}')
print('The oldest man is {}, who is {} years old.'.format(oldest_man_name, oldest_man_age))
print("We have {} women younger than 20.".format(total_women_20))

