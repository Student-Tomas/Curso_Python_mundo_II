# Challenge number 061: Create a arithimatic progression ap to the tenth term.
initial_term = int(input("Say the first term of the AP: "))
last_term = int(input("Say what is the last term: "))
progression = int(input("Say the progression ratio: "))
print((initial_term), end=" ")
while last_term > 1:
    print(("->"), end=" ")
    initial_term += progression
    last_term -= 1
    print((initial_term), end=" ")
print("-> End")
