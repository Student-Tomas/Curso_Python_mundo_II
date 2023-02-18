# Challenge number 063? Fibonacci Sequence.
terms = int(input("How many terms do you want to see? "))
t1 = 0
t2 = 1
cont = 2
print('{} => {} => '.format(t1, t2), end='')
while cont < terms:
    t3 = t1 + t2
    print('{} => '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print("The End!")
