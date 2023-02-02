# Challenge number 050: choose six numbers and show the sum of the evem ones.
print('Choose six numbers.')
sum = 0
count = 0
for n in range(6):
    numbers = int(input('Enter the number {}: '.format(n+1)))
    if numbers % 2 == 0:
        sum += numbers
        count += 1
print(f"You've informed {count} evem numbers and their sum is {sum}")
