# Challenge number 064: Sum all numbers typed by the user until receive the STOP Comand (999)
num = int(input("Say a number to be added (or 999 to stop): "))
total = num
cont = 0
while num != 999:
    total += num
    cont += 1
    num = int(input("Say a number to be added (or 999 to stop): "))
print(("<" * 10), end='')
print('>' * 10)
print(f"You entered {cont} numbers and the sum of then is {total}.")
