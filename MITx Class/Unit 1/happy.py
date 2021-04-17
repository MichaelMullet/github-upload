count = 0
maxCount = 0
result = 0
s = 'bababcbcde'

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        count += 1
        if count > maxCount:
            maxCount = count
            result = i+1
    else:
        count = 0

longest = s[result-maxCount:result+1]

print ("Longest substring in alphabetical order is: " + longest)