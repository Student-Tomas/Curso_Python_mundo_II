# Challenge 068: Create a "Even or Odd Game".
# The game will be finished when the user loose it.
from random import randint
while True:
    pc_number = randint(0, 5)
#    print(pc_number)
    user_choice = str(input("Choose (E) for even or (O) for odd: ")).strip().upper()
    if user_choice not in "EO":
        print("Choice invalid. Please, choose E for even or O for odd: ")
        user_choice = str(input("Choose (E) for even or (O) for odd: ")).strip().upper()
    user_number = (int(input("Type a number between 0 and 5: ")))
    if str(user_number) not in "012345":
        print("This value is not accepted. Enter a number between 0 and 5, please: ")
        user_number = (int(input("Type a number between 0 and 5: ")))
    result = (pc_number + user_number) % 2
    if result == 0:
        end_game = "O"
    else:
        end_game = "E"
    if end_game == user_choice:
        print("~~" * 10)
        print(f"You chose {user_choice} and put the number {user_number}, while the PC entered the number {pc_number}. Therefore, You win!!!!")
        print("~~" * 10)
    else:
        print("~~" * 10)
        print(f"You chose {user_choice} and put the number {user_number}, while the PC entered the number {pc_number}. Therefore, You loose!!!!")
        break
