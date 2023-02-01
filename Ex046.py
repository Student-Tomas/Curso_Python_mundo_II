# Chalenge number 046: make a countdown using "for" and some time between numbers.
from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(1)
print("LAUNCH !!!!!")

