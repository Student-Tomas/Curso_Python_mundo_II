# Challenge number 070: create a list of products and its prices. At the end show the total bill, how many products
# cost more than 1000, and what is the name of the cheapest product.
counter = sum = more_thousend = cheapest_price = cheapest_product = 0
while True:
    product = str(input("Product name: "))
    price = float(input("Product price: "))
    print("~~"*20)
    counter += 1
    if counter == 1:
        cheapest_price = price
        cheapest_product = product
    elif price > cheapest_price:
        cheapest_price = price
        cheapest_product = product
    sum += price
    if price >= 1000:
        more_thousend += 1
    add_more = ' '
    while add_more not in "YN":
        add_more = str(input("Do you want to add more products? ")).strip().upper()[0]
        print("~~" * 20)
    if add_more == "N":
        break
print(f"You have bought {counter} products and the total bill is {sum}.")
print(f"There are(is) {more_thousend} product(s) that cost(S) more than 1000.")
print(f"The cheapest product is the {cheapest_product} and it costs {cheapest_price}")

