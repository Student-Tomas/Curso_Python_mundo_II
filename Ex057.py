# Challenge number 057: make a program that reads the gender of a person and only ends when the user enters W or M.
answer = str(input("What is the gender? ")).strip().lower()
while answer != "w" and answer != "m":
        answer = str(input('Gender invalid! Please, enteer a valid gender option (W/M)? ')).strip().lower()
print("ok. Your gender was registered")

