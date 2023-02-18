# Challenge 062? Improve the ex 061 including a option for the user to ask for mor terms, until the user give up.
first_term = int(input("Say a number to be the first term of the AP: "))
terms = int(input("Say the initial number of terms: "))
ratio = int(input("Enter the AP's ratio: "))
while terms != 0:
    while terms > 0:
        print("{} -> ".format(first_term), end=" ")
        first_term += ratio
        terms -= 1
    print("Pause!!!")
    terms = int(input("How many more terms do you want? "))
print("The end!!!")
