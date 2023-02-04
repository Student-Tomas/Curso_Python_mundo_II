# Challenge 052: mark prime numbers.
num = int(input('Say a number: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(c), end='')
if total == 2:
    print('\n\033[mThe number {} was divided {} times, then it is PRIME'.format(num, total))
elif total == 1:
    print('\n\033[mThe number {} was divided only {} time, then it is NOT PRIME'.format(num, total))
else:
    print('\n\033[mThe number {} was divided {} times, then it is NOT PRIME'.format(num, total))

