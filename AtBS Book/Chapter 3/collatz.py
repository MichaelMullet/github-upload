def checkForOne(number):
    if number == 1:
        return number
    else:
        print(number)

def collatz(number):
    while True:
        if number % 2 == 0:
            number = number // 2
            if number == 1:
                return number
            else:
                print(number)
        else:
            number = 3 * number + 1
            if number == 1:
                return number
            else:
                print(number)

def cSequence():
    while True:
        try:
            userInput = input('Please type any integer, or \'q\' to quit. ')
            if userInput == 'q':
                return 'quitter'
            else:
                print(collatz(int(userInput)))
        except ValueError:
            print('Oops! That was no valid number. Try again.')

print(cSequence())