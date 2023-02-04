'''# Challenge number 047: make a count from 1 to 50 showing only the even numbers
for count in range(2, 51, 2):
    print("{} ".format(count), end="")'''

# There is another way to do it, however it will make two times more loops
for count in range(1, 51):
    if count % 2 == 0:
        print("{} ".format(count), end="")






