# Challenge number 069: creat a program that reads the age and the gender of many people.
# At the end, say how many are older than 18, how manu are male, and how many women are less than 20.
counter = male_counter = female_counter = 0
while True:
    age = int(input("What is the age? "))
    gender = str(input("what is the gender? Answer (M) for male and (F) for female. ")).strip().upper()[0]
    if gender