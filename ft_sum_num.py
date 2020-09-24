import ft_len_num as f


def ft_sum_num(a):
    if a < 0:
        a = -a
    n = f.ft_len_num(a)
    k = 0
    for i in range(n):
        k += a % 10
        a //= 10
    return k
