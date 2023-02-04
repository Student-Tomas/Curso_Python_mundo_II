# Challenge number 051: 10 terms of an arithmatic progression.
start = int(input('Say the first term: '))
ratio = int(input('Say the ratio: '))
tenth = start + (10 - 1) * ratio
for x in range(start, tenth + ratio, ratio):
    print('{}'.format(x), end=" -> ")
print("Done !!!!")

