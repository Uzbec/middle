def ft_covert_num(a, ss):
    k = 0
    m = 1
    if ss == 10:
        return a
    while a > 0:
        k += a % ss * m
        m *= 10
        a //= ss
    return k
