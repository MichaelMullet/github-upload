def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    List1 = L[:]
    for i in List1:
        if f(i) == False:
            L.remove(i)
    return len(L)
run_satisfiesF(L, satisfiesF)