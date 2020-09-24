def ft_bin_num(a):
    k = 0
    m = 1
    while a > 0:
        k += a % 2 * m
        m *= 10
        a //= 2
    return k
