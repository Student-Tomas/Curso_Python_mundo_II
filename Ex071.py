# Challenge 071: Create a program that emulate am ATM. This program has to say how many bills
# the user will receive, acording to the amont he or she wants. The ATM has only bills of 50, 20, 10 and 1
bill50 = count50 = bill20 = count20 = bill10 = count10 =bill1 = count1 = 0
amount = int(input("How much money do you want? "))
while True:
    if amount >= 50:
        bill50 += amount // 50
        amount = amount % 50
        count50 += 1
    if amount >= 20:
        bill20 += amount // 20
        amount = amount % 20
        count20 += 1
    if amount >= 10:
        bill10 += amount // 10
        amount = amount % 10
        count10 +=1
    if amount >= 1:
        bill1 += amount // 1
        amount = amount % 1
        count1 += 1
    if amount == 0:
        break
if count50 !=0:
    print(f"We have {bill50} fifty bills")
if count20 !=0:
    print(f"And we have {bill20} twenty bills")
if count10 !=0:
    print(f"And we have {bill10} ten bills")
if count1 !=0:
    print(f"And we have {bill1} one bills")






