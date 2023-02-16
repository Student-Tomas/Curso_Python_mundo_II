# Challenge number 060: factorial
# the easiest way is using the library Math and the function factorial.
'''from math import factorial
num = int(input("Say the number: "))
fac = factorial(num)
print('The factorial of {} is {}'.format(num, fac))'''

# Now, using "while"
'''num = int(input('Say a number: '))
c = num
fac = 1
while c > 0:
    print("{}".format(c), end=" ")
    if c > 1:
        print(("X"), end=" ")
    else:
        print(("="), end=" ")
    fac *= c
    c -= 1
print(fac)'''

# I'm gonna try to solve using "for"
num = int(input('Enter a number: '))
c = num #this is just a counter
fac = 1
for i in range(1, num + 1):
    fac *= c
    c -= 1
print("The factorial of {} is {}".format(num, fac))


