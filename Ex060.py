# Challenge number 060: factorial
# the easiest way is using the library Math and the function factorial.
'''from math import factorial
num = int(input("Say the number: "))
fac = factorial(num)
print('The factorial of {} is {}'.format(num, fac))'''

num = int(input('Enter a number: '))
seq = num
for i in range(6, 0):
    seq = num * i
print(seq)

