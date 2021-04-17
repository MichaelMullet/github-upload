import sys

number = int(input('Type any number. '))
even = number // 2
odd = 3 * number + 1

def collatz(number):
    if number % 2 == 0:
        print(even)
    elif number % 2 == 1:
        print(odd)

while True:
    if number == 1:
        sys.exit()
    else:
        collatz(number)

