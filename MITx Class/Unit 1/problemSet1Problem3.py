count = 0 # Variable that counts the current number of successive alphabetical letters
maxCount = 0 # Variable that counts the highest number of successive alphabetical letters
lastCount = 0 # Variable that indexes the last letter of the longest string in s
s = input('Please type a string of letters: ') # Letters typed by the user for the program to operate on

for i in range(len(s)-1): # Program loop that iterates over the number of letters in s
    try:
        if s[i] <= s[i+1]: # If the current letter is <= the next letter (letters have a numerical value)
            count += 1 # Count variable goes up by one
            if count > maxCount: # If count is greater than maxCount
                maxCount = count # Then maxCount is now count
                lastCount = i+1 # And the index of the last letter for maxCount is moved over one
        else: # If the current letter is less than the next letter
            count = 0 # Count is cleared, ready to start over in the next loop
    except ValueError:
        print('Please type a valid string.')


longest = s[lastCount-maxCount:lastCount+1] # The linked letters mapped to the maxCount in s

print ("Longest substring in alphabetical order is: " + longest) # The outcome of the program