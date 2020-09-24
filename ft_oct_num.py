def ft_oct_num(a):
    k = 0
    m = 1
    while a > 0:
        k += a % 8 * m
        m *= 10
        a //= 8
    return k
