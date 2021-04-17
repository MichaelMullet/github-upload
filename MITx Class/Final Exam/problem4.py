def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """
    countUp = 0
    maxCountUp = 0
    resultUp = []
    countDown = 0
    maxCountDown = 0
    resultDown = []
    for i in range(len(L)-1):
        if L[i] <= L[i+1]:
            countUp += 1
            if countUp > maxCountUp:
                maxCountUp = countUp
                resultUp.append(L[i])
        else:
            countUp = 0
    for i in range(len(L)-1):
        if L[i] >= L[i+1]:
            countDown += 1
            if countDown > maxCountDown:
                maxCountDown = countDown
                resultDown.append(L[i])
        else:
            countDown = 0
    if len(resultUp) >= len(resultDown):
        return sum(resultUp)
    else:
        return sum(resultDown)

print(longest_run([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))