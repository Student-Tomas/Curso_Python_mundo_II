# Challenge number 055: Say which weigth is the highest and the lowest.
'''Highest = 0
lowest = 0
for w in range(1, 6):
    weigth = float(input('Say the weigth of the {} person: '.format(w)))
    if w == 1:
        highest = weigth
        lowest = weigth
    else:
        if weigth > highest:
            highest = weigth
        if weigth < lowest:
            lowest = weigth
print('The highest weigth is {}.\nThe lowest weigth is {}.'. format(highest, lowest))'''

# this first algorithm was presented by the instructor, because we haven't learned lists yet.
# Below, we have the algorithm using lists.

list = []
for w in range(1,6):
    weight = float(input("{}ª person's weight: ".format(w)))
    list += [weight]
print('The highest weigth is {} and the lowest is {}'.format(max(list), min(list)))





