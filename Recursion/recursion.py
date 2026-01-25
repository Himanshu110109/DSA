## just a basic example for recursion don't laugh on it
def recursion(n):
    if n == 1:
        return 1
    return n + recursion(n-1)