def ft_pow(a, st):
    k = a
    if st > 0:
        for i in range(st - 1):
            a *= k
        return a
    elif st == 0:
        return 1
    for i in range(a):
        a /= k
    return a
