# Challlene number 067: Show the multiplication table of 'n' numbers
while True:
    num = int(input("Say the number you want to see its multiplication table: "))
    if num < 0:
        break
    for i in range(0, 11):
        print(f"{num} X {i} = {num*i}")
    print("If you want to stop the sequence, type a negative number:")
print("Sequence finished by user!!!")
