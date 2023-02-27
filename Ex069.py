# Challenge number 069: creat a program that reads the age and the gender of many people.
# At the end, say how many are older than 18, how manu are male, and how many women are less than 20.
age_counter = male_counter = female_counter = 0
while True:
    age = int(input("What is the age? "))
    gender = " "
    while gender not in "FM":
        gender = str(input("what is the gender? Answer (M) for male and (F) for female. ")).strip().upper()[0]
    print("~"*30)
    if age >= 18:
        age_counter += 1
    if gender == "F" and age < 20:
        female_counter += 1
    if gender == "M":
        male_counter += 1
    another_pearson = " "
    while another_pearson not in "YN":
        another_pearson = str(input("Do you want to continue? Yes (Y) or No (N) ")).strip().upper()[0]
    print("~" * 30)
    if another_pearson == "N":
        break
print("~"*30)
print(f"We have {age_counter} people who are more than 18. ")
print(f"We have {male_counter} men.")
print(f"And {female_counter} women are less than 20. ")

