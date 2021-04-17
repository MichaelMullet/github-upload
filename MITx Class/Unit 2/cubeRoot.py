cube = .5
epsilon = 0.01
num_guesses = 0
low = 1
fractionLow = 0
fractionHigh = 1
high = cube
guess = (high + low)/2.0
while abs(guess**3-cube) >= epsilon:
    if cube >= 1:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low)/2.0
        num_guesses += 1
    else:
        if guess**3 > cube:
            fractionLow = guess
        else:
            high = guess

print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)