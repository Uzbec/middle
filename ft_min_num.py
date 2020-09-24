import ft_len_num as f


def ft_min_num(a):
    n = f.ft_len_num(a)
    k = a % 10
    if a < 0:
        a = -a
    for i in range(n):
        if k > a % 10:
            k = a % 10
        a //= 10
    return k
