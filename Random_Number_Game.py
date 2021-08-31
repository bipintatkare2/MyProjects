# Project :- Random Number Guessing
# Still in progress

from random import randint

player = 0
num = int(input("Enter Number: "))
auto_num = randint(0, 2)
print("Random number is : {}".format(auto_num))

if num == auto_num:
    print(player+1)
