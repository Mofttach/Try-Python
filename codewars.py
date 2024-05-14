def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    a = []

    for i in range(1, n+1):
        b = i * x
        a.append(b)
    
    return a


print(count_by(2,5))