import ft_len_num as f


def ft_rev_num(l):
    a = l
    n = f.ft_len_num(a)
    k = 0
    if a < 0:
        a = -a
    for i in range(n):
        m = a % 10
        k = k * 10 + m
        a //= 10
    return k if l > 0 else -k
