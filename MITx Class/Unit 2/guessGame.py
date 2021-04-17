epsilon = 0.01
low = 0
high = 100
guess = (high + low)//2.0
numGuess = 0
print('Please think of a number between 0 and 100!')
while abs(guess) >= epsilon:
    print('Is your secret number ' + str(guess) + '?')
    poo = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if poo == 'h':
        high = guess
    elif poo == 'l':
        low = guess
    elif poo == 'c':
        print('Game over. Your secret number was ' + str(guess))
        break
    else:
        print('Sorry, I did not understand your input.')
    guess = (high + low)//2.0
    numGuess += 1
print('Number of guesses = ' + str(numGuess + 1))