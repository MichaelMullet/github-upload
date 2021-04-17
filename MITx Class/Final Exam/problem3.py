def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    if n // 6 == 0 and n // 9 == 0 or n // 6 == 0 and n // 20 == 0 or n // 9 == 0 and n // 20 == 0:
        return True
    else:
        return False

print(McNuggets(15))