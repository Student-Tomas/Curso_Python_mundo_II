# Challenge number 066? Enter a serie of numbers and present the sum, without the comand to stop.
num = counter = sum = 0
while num != 999:
    num = int(input("Say a number, or type 999 to stop the sequence: "))
    if num == 999:
        break
    sum += num
    counter += 1
print(f"You entered {counter} numbers and the sum of then is {sum}")
