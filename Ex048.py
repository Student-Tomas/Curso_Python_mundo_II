# Challenge number 048: sum of all odd and multiples of three between 1 and 500.
sum = 0
count = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        count += 1
        sum += c
print('We have {} numbers in this range and the sum of then is {}'.format(count, sum))

