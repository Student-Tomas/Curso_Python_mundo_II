# Chalenge number 049: build a multiplication table.
x = int(input('choose the number with which you would like to see the multiplication table: '))
for n in range(0, 11):
    result = x * n
    print('{} X {} = {}'.format(x, n, result))
