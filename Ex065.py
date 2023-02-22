# Challenge number 065: Give the average, the greater and the smaller number of the list entered by the user
answer = ""
counter = sum = greater = smaller = 0
while answer in "Yy":
    num = int(input("Say a number: "))
    counter += 1
    sum += num
    if counter == 1:
        greater = smaller = num
    else:
        if num > greater:
            greater = num
        if num < smaller:
            num = smaller
    answer = str(input("Do you want to continue? (Y or N?) "))
    if answer not in "YyNn":
        print("The answer is not valid. Please, enter Y for Yes or N for NO:")
        print(f"Please answer the question again.")
        answer = str(input("Do you want to continue? (Y or N?) "))
print(f"You entered {counter} numbers and the average between then is {sum / counter}")
print(f"The biggest number entered was {greater} and the smallest was {smaller}")




