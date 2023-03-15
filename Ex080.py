# Challenge number 080: create a program that receive five numbers from the user and put them in a ordered list, without using "sort()"
list = []
greater = 0
smaller = 0
for i in range(0, 5):
    num = int(input('Say a number: '))
    list.append(num)
    ask = str(input('Do you want to continue? [Y/N] ')).strip().upper()
    if ask not in 'YN':
        print('=='*30)
        print('Invalid answer. Please try again.')
        print('==' * 30)
    if ask == 'N':
        print('Good bye!!!')
        break
print(list)
